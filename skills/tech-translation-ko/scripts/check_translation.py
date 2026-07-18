#!/usr/bin/env python3
"""번역 결과 기계 검사(lint).

Usage:
    python3 check_translation.py TRANSLATED.md [--source ORIGINAL.md] [--glossary GLOSSARY.tsv] [--format text|json]

결정적으로 판별 가능한 번역 규칙 위반을 검사한다. 등급은 두 가지다.

- error: 확실한 위반. 반드시 수정한다.
- warning: 검토 필요. 문맥상 허용될 수 있으므로 사람이나 LLM이 판단한다.

--source 를 주면 마크다운 구조(줄 수, 코드블록 수, 헤딩 레벨, 링크 수)를
원문과 대조한다. ko.javascript.info 계열 프로젝트는 줄 수 보존이 필수 규칙이다.
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

RULES_DOC = {
    "KO-E001": "em-dash(—) 사용 금지. 쉼표·마침표·괄호로 대체",
    "KO-E002": "문장 끝 쌍점(:) 금지. 리스트 라벨 뒤 쌍점은 허용",
    "KO-E003": "헤딩 끝에 마침표·느낌표 금지(물음표는 실제 코퍼스 관행상 허용)",
    "KO-E004": "짝 단어는 슬래시(/) 대신 가운뎃점(·) 사용",
    "KO-E005": "괄호 앞 마침표 금지. '문장했다.(부연)' → '문장했다(부연).'",
    "KO-E101": "원문과 줄 수 불일치",
    "KO-E102": "원문과 코드블록(펜스) 수 불일치",
    "KO-E103": "원문과 헤딩 수·레벨 불일치",
    "KO-E104": "원문과 링크 URL 불일치(누락·변형)",
    "KO-W001": "이중 피동 의심(보여지다·쓰여지다·생각되어지다 등)",
    "KO-W002": "번역투 의심 표현",
    "KO-W003": "용어집과 다른 역어 사용 의심",
    "KO-W004": "복수 접미사 '~들' 남용 의심(한 문장에 2회 이상)",
    "KO-W005": "인칭대명사(당신·여러분·우리들) 직역 의심",
    "KO-W006": "'만약' 관용 점검(뒤따르는 '-면'이 있으면 생략 가능)",
    "KO-W007": "명사 종결 문장 뒤 마침표 의심(리스트 항목)",
    "KO-W008": "큰따옴표 강조 의심(직접 인용이 아니면 작은따옴표)",
    "KO-E006": "자주 틀리는 말(KIGO): 그리고 나서→그러고 나서, 몇 일→며칠 등",
    "KO-W009": "격조사 '~의' 연속 사용 의심(KIGO)",
    "KO-W010": "미래 시제 직역 의심: '~할 것입니다'는 현재형 권장(KIGO)",
    "KO-W011": "숫자와 단위 사이 공백 의심: IT 분야는 붙여 씀(KIGO)",
}

# KIGO 자주 틀리는 말: (오류 정규식, 교정)
KIGO_MISSPELL = [
    (r"그리고 나서", "그러고 나서"),
    (r"몇 ?일(?= [동안이후뒤])|몇일", "며칠"),
    (r"하므로써", "함으로써"),
    (r"삼가하", "삼가"),
    (r"잠궈|잠구", "잠가/잠그"),
    (r"예/아니오", "예/아니요"),
]

# 번역투 패턴: (정규식, 제안)
TRANSLATIONESE = [
    (r"~?에 대해[서]? 알아보도록 하겠습니다", "'~을 알아봅시다'처럼 간결하게"),
    (r"하는 것이 가능합니다", "'할 수 있습니다'로"),
    (r"필요로 합니다", "'필요합니다'로"),
    (r"존재하지 않습니다", "문맥에 따라 '없습니다'로"),
    (r"가지고 있[습는]", "문맥에 따라 '있습니다/입니다'로"),
    (r"에 의해서?\s", "능동형으로 재구성 검토"),
    (r"를 통해서?\s", "'~로', '~를 사용해' 등으로 검토"),
    (r"으로부터", "'에서'로 검토"),
    (r"에 있어서?\s", "조사 정리 검토"),
    (r"그것[은이을]", "지시 대상을 명시"),
    (r"이것[은이을]", "지시 대상을 명시"),
]

DOUBLE_PASSIVE = re.compile(
    r"(보여지|쓰여지|만들어지게 되|생각되어지|불리워지|잊혀지|모여지|나뉘어지|믿겨지|읽혀지)"
)

PRONOUN = re.compile(r"(당신[은이의을]|여러분[은이의을]?의|우리들)")

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
FENCE = re.compile(r"^\s*(```|~~~)")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def is_hangul_text(line: str) -> bool:
    return any("HANGUL" in unicodedata.name(ch, "") for ch in line)


def strip_inline_code(line: str) -> str:
    return re.sub(r"`[^`]*`", "`C`", line)


def iter_prose_lines(lines):
    """코드블록 밖 라인만 (번호, 원본, 인라인코드 제거본)으로 순회한다.

    코드블록 안이라도 한글 주석 라인은 산문 규칙 대상이다(주석도 자연어).
    """
    in_fence = False
    for i, raw in enumerate(lines, 1):
        if FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            comment = re.search(r"(?://|#|<!--)\s*(.*)", raw)
            if comment and is_hangul_text(comment.group(1)):
                yield i, raw, strip_inline_code(comment.group(1)), True
            continue
        yield i, raw, strip_inline_code(raw), False


def check_content(lines):
    findings = []

    def add(rule, line_no, excerpt, note=""):
        findings.append({
            "rule": rule,
            "severity": "error" if rule.startswith("KO-E") else "warning",
            "line": line_no,
            "excerpt": excerpt.strip()[:120],
            "message": RULES_DOC[rule] + (f" ({note})" if note else ""),
        })

    for no, raw, text, is_comment in iter_prose_lines(lines):
        if not is_hangul_text(text):
            continue

        if "—" in text:
            add("KO-E001", no, raw)

        # 문장 끝 쌍점: 라벨형(**라벨:** 또는 '단어:'가 짧은 리스트 라벨)은 허용
        stripped = text.rstrip()
        if stripped.endswith(":") and not raw.lstrip().startswith(("|",)):
            label_like = re.search(r"(^|[-*+]\s|\*\*)[^.!?]{1,25}:$", stripped)
            if not label_like or re.search(r"[다요]\s*:$", stripped):
                add("KO-E002", no, raw)

        m = HEADING.match(raw)
        if m and re.search(r"[.!。]\s*$", m.group(2).strip()):
            add("KO-E003", no, raw)

        # 짝 단어 슬래시: 한글단어/한글단어 (URL·코드 제외)
        if re.search(r"[가-힣]{1,6}/[가-힣]{1,6}", text):
            add("KO-E004", no, raw)

        # 마침표+괄호: 괄호 안이 구(마침표로 안 끝남)이면 위반. 괄호 안 완결 문장은 허용
        m_paren = re.search(r"[다요]\.\s*\(([^)]*)\)", text)
        if m_paren and not m_paren.group(1).rstrip().endswith("."):
            add("KO-E005", no, raw)

        if DOUBLE_PASSIVE.search(text):
            add("KO-W001", no, raw)

        for pat, hint in TRANSLATIONESE:
            if re.search(pat, text):
                add("KO-W002", no, raw, hint)

        if len(re.findall(r"[가-힣]+들[이은을과의에도]?[\s,.]", text)) >= 2:
            add("KO-W004", no, raw)

        if PRONOUN.search(text):
            add("KO-W005", no, raw)

        if re.search(r"만약", text) and re.search(r"[다면라면]면", text):
            add("KO-W006", no, raw)

        if re.match(r"^\s*[-*+]\s+.*[가-힣]\.\s*$", raw) and not re.search(r"(니다|세요|시오|이다|한다)\.\s*$", raw):
            add("KO-W007", no, raw)

        if re.search(r"[\"“][가-힣][^\"”]{0,20}[\"”]", text) and not re.search(r"(말했|물었|답했|라고)", text):
            add("KO-W008", no, raw)

        for pat, correction in KIGO_MISSPELL:
            if re.search(pat, text):
                add("KO-E006", no, raw, f"→ {correction}")

        if re.search(r"[가-힣]+의\s+[가-힣]+의\s", text):
            add("KO-W009", no, raw)

        m_fut = re.search(r"([가-힣])\s?것입니다", text)
        if m_fut and (ord(m_fut.group(1)) - 0xAC00) % 28 == 8:  # 받침이 ㄹ인 관형형
            add("KO-W010", no, raw)

        if re.search(r"\d[\d,.]*\s+(kg|km|cm|mm|ms|kb|mb|gb|tb|mbps|gbps|바이트|비트|픽셀)(?![A-Za-z0-9])", text, re.IGNORECASE):
            add("KO-W011", no, raw)

    return findings


def check_structure(src_lines, dst_lines):
    findings = []

    def add(rule, line_no, msg):
        findings.append({
            "rule": rule, "severity": "error", "line": line_no,
            "excerpt": "", "message": RULES_DOC[rule] + " " + msg,
        })

    if len(src_lines) != len(dst_lines):
        add("KO-E101", 1, f"원문 {len(src_lines)}줄, 번역 {len(dst_lines)}줄")

    sf = sum(1 for l in src_lines if FENCE.match(l))
    df = sum(1 for l in dst_lines if FENCE.match(l))
    if sf != df:
        add("KO-E102", 1, f"원문 펜스 {sf}개, 번역 {df}개")

    sh = [HEADING.match(l).group(1) for l in src_lines if HEADING.match(l)]
    dh = [HEADING.match(l).group(1) for l in dst_lines if HEADING.match(l)]
    if sh != dh:
        add("KO-E103", 1, f"원문 헤딩 {len(sh)}개{sh}, 번역 {len(dh)}개{dh}")

    s_urls = [u for l in src_lines for u in LINK.findall(l)]
    d_urls = [u for l in dst_lines for u in LINK.findall(l)]
    if len(s_urls) != len(d_urls):
        add("KO-E104", 1, f"원문 링크 {len(s_urls)}개, 번역 {len(d_urls)}개")

    return findings


def check_glossary(lines, glossary_path):
    """용어집 위반 후보 검출. 원어가 본문에 남아있는데 등재 역어가 없는 경우 등은
    문맥 판단이 필요하므로 warning으로만 보고한다."""
    findings = []
    rows = []
    for row in Path(glossary_path).read_text(encoding="utf-8").splitlines()[1:]:
        cols = row.split("\t")
        if len(cols) >= 2 and re.fullmatch(r"[A-Za-z][A-Za-z ().'/,-]+", cols[0]):
            rows.append((cols[0].strip(), cols[1].strip()))

    text_all = "\n".join(l for _, _, l, _ in iter_prose_lines(lines))
    # 튜토리얼 내부 링크 문법(<info:anchor-slug>)은 식별자이므로 검사 제외
    text_all = re.sub(r"<info:[^>]*>", "<info:X>", text_all)
    # 한-영 병기 구간: 한글 바로 뒤 괄호 안의 원어는 이미 번역된 것이므로 검사 제외
    annotated_spans = [m.span(1) for m in re.finditer(r"[가-힣»)]\(([^)]*)\)", text_all)]

    def outside_annotation(m):
        return not any(a <= m.start() and m.end() <= b for a, b in annotated_spans)

    for en, ko in rows:
        if ko in ("번역 안함", "번역안함") or en.lower() == ko.lower():
            continue
        alternatives = [a.strip() for a in re.split(r"[,/]", ko) if re.search(r"[가-힣]", a)]
        if not alternatives:
            continue
        # 원어가 산문에 단어로 등장하고(병기 괄호·제품명 제외) 등재 역어가 하나도 없으면 의심
        matches = [m for m in re.finditer(
            rf"(?<![\w`.]){re.escape(en)}(?![\w`]|\.\w)", text_all, re.IGNORECASE)
            if outside_annotation(m)]
        if matches and not any(alt in text_all for alt in alternatives):
            findings.append({
                "rule": "KO-W003", "severity": "warning", "line": 0,
                "excerpt": en,
                "message": RULES_DOC["KO-W003"] + f" ('{en}' → 등재 역어 '{ko}')",
            })
    return findings


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("translated")
    ap.add_argument("--source")
    ap.add_argument("--glossary")
    ap.add_argument("--format", choices=["text", "json"], default="text")
    args = ap.parse_args()

    dst_lines = Path(args.translated).read_text(encoding="utf-8").splitlines()
    findings = check_content(dst_lines)

    if args.source:
        src_lines = Path(args.source).read_text(encoding="utf-8").splitlines()
        findings += check_structure(src_lines, dst_lines)

    if args.glossary:
        findings += check_glossary(dst_lines, args.glossary)

    findings.sort(key=lambda f: (f["severity"] != "error", f["line"]))
    errors = sum(1 for f in findings if f["severity"] == "error")
    warnings = len(findings) - errors

    if args.format == "json":
        print(json.dumps({"errors": errors, "warnings": warnings, "findings": findings},
                         ensure_ascii=False, indent=1))
    else:
        for f in findings:
            loc = f"{args.translated}:{f['line']}" if f["line"] else args.translated
            print(f"{f['severity'].upper():7} {f['rule']} {loc}  {f['message']}")
            if f["excerpt"]:
                print(f"        > {f['excerpt']}")
        print(f"\n{errors} error(s), {warnings} warning(s)")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
