#!/usr/bin/env python3
"""
ko.javascript.info / en.javascript.info corpus manifest builder.

지정된 저자(대상: Bora Lee 계열 git author name 전체, 실제로는 동일 이메일로
식별되는 여러 표기 변형을 포함)가 건드린 .md 파일을 ko 저장소 전체 이력에서
전수 수집하고, 파일별 커밋 통계·blame 기반 기여 비율·변경 유형 분류·en 저장소
대응 경로 및 시점 리비전을 계산해 manifest.json / manifest_summary.tsv로
출력한다.

PII 주의: 커밋 이메일은 매칭에만 내부적으로 사용하고 출력에는 절대 기록하지
않는다. 출력에는 git author name만 남긴다.
"""

import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

KO_REPO = Path("/Users/bora/experiments/js-info/ko.javascript.info")
EN_REPO = Path("/Users/bora/experiments/js-info/en.javascript.info")
OUT_DIR = Path("/Users/bora/experiments/tech-translation-ko/docs/analysis")
MANIFEST_JSON = OUT_DIR / "manifest.json"
MANIFEST_TSV = OUT_DIR / "manifest_summary.tsv"

# 지시된 3개 이름 리터럴(대소문자 무시, 참고용 비교 통계에 사용)
TARGET_NAME_LITERALS = {"violet bora lee", "bora lee", "violet.lee"}

# 실제 매칭 기준: 위 세 이름과 동일 인물임이 이메일로 확인된 author 이름 전체.
# git log 조회로 실제 저장소에서 확인한 값이며 이메일은 매칭에만 쓰고 출력하지 않는다.
TARGET_AUTHOR_NAMES = {
    "bora lee",
    "bora lee (violet)",
    "violet bora lee",
    "violet-bora-lee",
    "violet.lee",
    "이보라",
    "desktop-3vc7vhh\\learn",
}


def run(cmd, cwd, check=True):
    result = subprocess.run(
        cmd, cwd=cwd, capture_output=True, text=True, check=False
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"cmd failed: {cmd}\n{result.stderr}")
    return result.stdout


def eprint(*args):
    print(*args, file=sys.stderr, flush=True)


def get_current_md_files():
    out = run(["git", "ls-files", "*.md"], cwd=KO_REPO)
    return sorted(l for l in out.splitlines() if l.strip())


def get_all_historical_md_paths():
    """target author가 이력상 건드린 모든 .md 경로(당시 파일명 기준)."""
    out = run(
        [
            "git",
            "log",
            "--no-merges",
            "--name-only",
            "--pretty=format:",
            "--",
            "*.md",
        ],
        cwd=KO_REPO,
    )
    all_paths = set(l for l in out.splitlines() if l.strip())

    # 저자 필터링을 위해 커밋 해시별 author를 별도로 얻어 교집합 구성
    log_out = run(
        [
            "git",
            "log",
            "--no-merges",
            "--pretty=format:COMMIT|%H|%an",
            "--name-only",
            "--",
            "*.md",
        ],
        cwd=KO_REPO,
    )
    touched = set()
    cur_author = None
    for line in log_out.splitlines():
        if line.startswith("COMMIT|"):
            _, _h, an = line.split("|", 2)
            cur_author = an.strip().lower()
        elif line.strip():
            if cur_author in TARGET_AUTHOR_NAMES:
                touched.add(line.strip())
    return touched, all_paths


def get_file_history_and_bora_commits(path):
    """
    현재 파일 path의 rename 이력을 --follow로 전부 추적.
    반환: (historical_names:set, bora_commits:list[dict])
    """
    out = run(
        [
            "git",
            "log",
            "--follow",
            "--no-merges",
            "--numstat",
            "--pretty=format:COMMIT|%H|%ai|%an",
            "--",
            path,
        ],
        cwd=KO_REPO,
    )
    historical_names = set()
    bora_commits = []
    cur = None
    for line in out.splitlines():
        if line.startswith("COMMIT|"):
            _, h, ai, an = line.split("|", 3)
            cur = {
                "hash": h,
                "date": ai.strip(),
                "author_name": an.strip(),
                "insertions": 0,
                "deletions": 0,
            }
        elif line.strip():
            parts = line.split("\t")
            if len(parts) == 3:
                add, dele, fname = parts
                historical_names.add(fname)
                if cur is not None:
                    try:
                        cur["insertions"] += int(add)
                    except ValueError:
                        pass
                    try:
                        cur["deletions"] += int(dele)
                    except ValueError:
                        pass
        else:
            if cur is not None and cur["author_name"].lower() in TARGET_AUTHOR_NAMES:
                bora_commits.append(cur)
            cur = None
    if cur is not None and cur["author_name"].lower() in TARGET_AUTHOR_NAMES:
        bora_commits.append(cur)
    return historical_names, bora_commits


def blame_share(path):
    """git blame -w --line-porcelain으로 현재 파일 라인별 author 집계."""
    out = run(
        ["git", "blame", "-w", "--line-porcelain", "--", path],
        cwd=KO_REPO,
        check=False,
    )
    total = 0
    bora = 0
    cur_author = None
    for line in out.splitlines():
        if line.startswith("author "):
            cur_author = line[len("author "):].strip().lower()
        elif line.startswith("\t"):
            total += 1
            if cur_author in TARGET_AUTHOR_NAMES:
                bora += 1
    return bora, total


def classify(share):
    if share >= 0.7:
        return "new_translation", "확정"
    elif share >= 0.2:
        return "mixed", "개연"
    else:
        return "review_edit", "개연"


def en_revision_for_date(date_iso):
    """date_iso(예: 2021-05-03 12:00:00 +0900) 이전 시점 en 저장소 최신 커밋."""
    date_only = date_iso.split(" ")[0]
    out = run(
        ["git", "rev-list", "-1", f"--before={date_only} 23:59:59", "master"],
        cwd=EN_REPO,
        check=False,
    )
    out = out.strip()
    return out if out else None


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    eprint("[1/4] 현재 ko 저장소 .md 파일 목록 수집 중...")
    current_files = get_current_md_files()
    eprint(f"  현재 .md 파일 수: {len(current_files)}")

    eprint("[2/4] 대상 저자 이력 전수 스캔 중 (rename 추적 포함)...")
    touched_hist_names, all_hist_names = get_all_historical_md_paths()
    eprint(f"  이력상 target author가 건드린 경로(당시 파일명) 수: {len(touched_hist_names)}")

    manifest_entries = {}
    all_current_historical_names = set()

    for i, path in enumerate(current_files, 1):
        if i % 100 == 0 or i == len(current_files):
            eprint(f"  [{i}/{len(current_files)}] {path}")
        hist_names, bora_commits = get_file_history_and_bora_commits(path)
        all_current_historical_names |= hist_names
        if not bora_commits:
            continue

        bora_lines, total_lines = blame_share(path)
        share = (bora_lines / total_lines) if total_lines else 0.0
        change_type, confidence = classify(share)

        last_date = max(c["date"] for c in bora_commits)
        en_path_candidate = EN_REPO / path
        en_path = path if en_path_candidate.exists() else None
        en_rev = en_revision_for_date(last_date) if en_path else None

        manifest_entries[path] = {
            "path": path,
            "bora_commits": {
                "count": len(bora_commits),
                "hashes": [c["hash"] for c in bora_commits],
                "commits": [
                    {
                        "hash": c["hash"],
                        "date": c["date"],
                        "author_name": c["author_name"],
                        "insertions": c["insertions"],
                        "deletions": c["deletions"],
                    }
                    for c in bora_commits
                ],
            },
            "bora_added_share": round(share, 4),
            "blame_bora_lines": bora_lines,
            "blame_total_lines": total_lines,
            "change_type": change_type,
            "confidence": confidence,
            "en_path": en_path,
            "en_revision": en_rev,
            "last_bora_commit_date": last_date,
        }

    eprint("[3/4] excluded(현재 미존재) 파일 목록 계산 중...")
    excluded_paths = sorted(touched_hist_names - all_current_historical_names)
    excluded_entries = []
    for path in excluded_paths:
        # 해당 경로가 등장하는 커밋(당시 파일명 기준)의 bora 커밋 통계만 별도 조회
        out = run(
            [
                "git",
                "log",
                "--no-merges",
                "--pretty=format:COMMIT|%H|%ai|%an",
                "--",
                path,
            ],
            cwd=KO_REPO,
        )
        cnt = 0
        hashes = []
        for line in out.splitlines():
            if line.startswith("COMMIT|"):
                _, h, _ai, an = line.split("|", 3)
                if an.strip().lower() in TARGET_AUTHOR_NAMES:
                    cnt += 1
                    hashes.append(h)
        excluded_entries.append(
            {"path": path, "bora_commits_count": cnt, "bora_commit_hashes": hashes}
        )

    eprint(f"  excluded 파일 수: {len(excluded_entries)}")

    eprint("[4/4] 결과 파일 기록 중...")
    manifest_out = {
        "matching_method": {
            "note": (
                "지시된 리터럴 3개 이름(Violet Bora Lee, Bora Lee, Violet.Lee) 외에 "
                "동일 이메일(사용자 본인 이메일)로 확인된 표기 변형을 모두 포함해 매칭함. "
                "이메일 자체는 출력에 포함하지 않음."
            ),
            "target_author_names": sorted(TARGET_AUTHOR_NAMES),
        },
        "files": manifest_entries,
        "excluded": excluded_entries,
    }
    MANIFEST_JSON.write_text(
        json.dumps(manifest_out, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    with MANIFEST_TSV.open("w", encoding="utf-8") as f:
        f.write("path\tchange_type\tconfidence\tbora_added_share\tbora_commits_count\ten_path_exists\n")
        for path, e in sorted(manifest_entries.items()):
            f.write(
                f"{path}\t{e['change_type']}\t{e['confidence']}\t"
                f"{e['bora_added_share']}\t{e['bora_commits']['count']}\t"
                f"{'yes' if e['en_path'] else 'no'}\n"
            )

    # ---- stdout 통계 요약 ----
    print("=== manifest 생성 완료 ===")
    print(f"총 포함 파일 수: {len(manifest_entries)}")
    print(f"excluded(현재 미존재) 파일 수: {len(excluded_entries)}")
    print()

    type_counts = defaultdict(int)
    for e in manifest_entries.values():
        type_counts[e["change_type"]] += 1
    print("[변경 유형별 파일 수]")
    for t in ("new_translation", "mixed", "review_edit"):
        print(f"  {t}: {type_counts.get(t, 0)}")
    print()

    conf_counts = defaultdict(int)
    for e in manifest_entries.values():
        conf_counts[e["confidence"]] += 1
    print("[신뢰도별 파일 수]")
    for c in ("확정", "개연"):
        print(f"  {c}: {conf_counts.get(c, 0)}")
    print()

    chapter_counts = defaultdict(lambda: defaultdict(int))
    for path, e in manifest_entries.items():
        chapter = path.split("/")[0]
        chapter_counts[chapter][e["change_type"]] += 1
    print("[챕터별 분포]")
    for chapter in sorted(chapter_counts):
        row = chapter_counts[chapter]
        total = sum(row.values())
        print(
            f"  {chapter}: total={total} "
            f"new_translation={row.get('new_translation',0)} "
            f"mixed={row.get('mixed',0)} "
            f"review_edit={row.get('review_edit',0)}"
        )
    print()

    review_edit_commit_total = sum(
        e["bora_commits"]["count"]
        for e in manifest_entries.values()
        if e["change_type"] == "review_edit"
    )
    print(f"교정(review_edit) 파일에 달린 bora 커밋 총합: {review_edit_commit_total}")
    total_bora_commits = sum(e["bora_commits"]["count"] for e in manifest_entries.values())
    print(f"포함 파일 전체 bora 커밋 총합(중복 포함, 파일 단위 합산): {total_bora_commits}")

    en_missing = sum(1 for e in manifest_entries.values() if not e["en_path"])
    print(f"en 대응 파일 없음: {en_missing} / {len(manifest_entries)}")

    print()
    print(f"출력: {MANIFEST_JSON}")
    print(f"출력: {MANIFEST_TSV}")


if __name__ == "__main__":
    main()
