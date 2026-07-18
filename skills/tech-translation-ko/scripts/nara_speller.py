#!/usr/bin/env python3
"""나라 맞춤법 검사기(바른한글, nara-speller.co.kr) 연동 도우미.

검사기 API(`POST /api/check`)는 Cloudflare 뒤에 있어 브라우저 컨텍스트에서만
호출할 수 있다. 이 스크립트는 브라우저 호출 전후의 결정적 작업을 맡는다.

** 이용 예절(중요) **
바른한글은 대학 연구실이 무료로 운영하는 서비스다. 반드시 수동으로, 사람이 지켜보는
가운데 실행한다. CI·크론·번역 파이프라인에 자동 호출을 넣지 말 것. 요청 사이엔
최소 0.4초 이상 지연을 두고, 같은 문서를 반복 검사하지 않는다.

Usage:
    python3 nara_speller.py prepare TRANSLATED.md > payload.json
    (브라우저에서 payload.json의 각 청크를 /api/check 로 전송해 results.json 저장)
    python3 nara_speller.py report TRANSLATED.md results.json

prepare: 마크다운에서 산문(코드블록 밖 + 코드 내 한글 주석)만 추출해
         검사기 요청 단위(기본 700자)로 청크를 만든다. 각 청크에 원본 줄 번호
         매핑을 담는다. 출력은 JSON:
         {"chunks": [{"id": 0, "text": "...", "lines": [[줄번호, 시작오프셋, 끝오프셋], ...]}]}

report:  브라우저에서 받아온 응답 배열(results.json:
         [{"id": 0, "errInfo": [...]}, ...])을 원본 줄 번호로 되돌려
         린터와 같은 형식으로 출력한다. 교정 후보가 있으면 exit code 1.

브라우저 쪽 호출 예시(개발자 콘솔 또는 자동화 도구에서, nara-speller.co.kr 탭):
    const payload = /* payload.json 내용 */;
    const out = [];
    for (const c of payload.chunks) {
      const r = await fetch('/api/check', {method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({text: c.text})});
      out.push({id: c.id, ...(await r.json())});
    }
    JSON.stringify(out)  // 이 결과를 results.json 으로 저장
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

FENCE = re.compile(r"^\s*(```|~~~)")
CHUNK_LIMIT = 700  # 검사기 1회 요청에 담을 최대 글자 수


def is_hangul_text(line: str) -> bool:
    return any("HANGUL" in unicodedata.name(ch, "") for ch in line)


def prose_lines(lines):
    """(줄번호, 검사 대상 텍스트) 목록. 코드블록 밖 산문과 코드 내 한글 주석."""
    in_fence = False
    for i, raw in enumerate(lines, 1):
        if FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            m = re.search(r"(?://|#|<!--)\s*(.*)", raw)
            if m and is_hangul_text(m.group(1)):
                yield i, m.group(1)
            continue
        if is_hangul_text(raw):
            # 인라인 코드·링크 URL은 검사에서 제외(검사기 오탐 방지)
            text = re.sub(r"`[^`]*`", " ", raw)
            text = re.sub(r"\]\([^)]*\)", "] ", text)
            text = re.sub(r"<info:[^>]*>", " ", text)
            yield i, text.strip()


def cmd_prepare(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    chunks, cur_texts, cur_lines, cur_len, cid = [], [], [], 0, 0
    for no, text in prose_lines(lines):
        if cur_len + len(text) + 1 > CHUNK_LIMIT and cur_texts:
            chunks.append({"id": cid, "text": "\n".join(cur_texts), "lines": cur_lines})
            cid, cur_texts, cur_lines, cur_len = cid + 1, [], [], 0
        start = cur_len + (1 if cur_texts else 0)
        cur_texts.append(text)
        cur_len = start + len(text)
        cur_lines.append([no, start, cur_len])
    if cur_texts:
        chunks.append({"id": cid, "text": "\n".join(cur_texts), "lines": cur_lines})
    json.dump({"file": str(path), "chunks": chunks}, sys.stdout, ensure_ascii=False)
    print(file=sys.stderr)
    print(f"청크 {len(chunks)}개, 산문 {sum(len(c['lines']) for c in chunks)}줄", file=sys.stderr)


def cmd_report(path, results_path):
    payload_lines = {}
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    # prepare와 동일한 청크를 재구성해 오프셋→줄 매핑을 만든다
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        cmd_prepare(path)
    chunks = {c["id"]: c for c in json.loads(buf.getvalue())["chunks"]}

    results = json.loads(Path(results_path).read_text(encoding="utf-8"))
    findings = skipped = style = 0
    for r in results:
        chunk = chunks.get(r.get("id"))
        if not chunk:
            continue
        for err in r.get("errInfo", []):
            org = err.get("orgStr", "")
            help_full = err.get("help", "")
            help_text = re.split(r"<br\s*/?>", help_full)[0].strip()
            # 오탐 필터: prepare가 인라인 코드를 지운 자리의 고아 조사·마커·영어 지적
            if (re.search(r"(^|\s)[을를이가은는의로에]\s*($|\s)", org)
                    or "- --" in org or "###" in org
                    or not re.search(r"[가-힣]", org)
                    or "영어 단어" in help_full):
                skipped += 1
                continue
            start = err.get("start", 0)
            line_no = next((ln for ln, s, e in chunk["lines"] if s <= start < e), "?")
            cand = err.get("candWord", "").replace("|", " / ")
            # 외래어 순화 제안은 참고 등급: 기술 용어집이 검사기보다 우선한다
            if "외래어" in help_full or "우리말로" in help_full:
                style += 1
                print(f"STYLE   {path}:{line_no}  {org} → {cand}  (용어집 등재어면 무시)")
                continue
            print(f"SPELL   {path}:{line_no}  {org} → {cand}")
            if help_text:
                print(f"        {help_text}")
            findings += 1
    print(f"\nSPELL {findings}건 / STYLE(순화 제안) {style}건 / 오탐 필터 제외 {skipped}건")
    sys.exit(1 if findings else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("prepare")
    p1.add_argument("file")
    p2 = sub.add_parser("report")
    p2.add_argument("file")
    p2.add_argument("results")
    args = ap.parse_args()
    if args.cmd == "prepare":
        cmd_prepare(args.file)
    else:
        cmd_report(args.file, args.results)


if __name__ == "__main__":
    main()
