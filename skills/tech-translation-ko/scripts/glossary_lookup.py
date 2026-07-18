#!/usr/bin/env python3
"""용어집 조회·원문 용어 추출.

Usage:
    python3 glossary_lookup.py --glossary GLOSSARY.tsv lookup <term>...
    python3 glossary_lookup.py --glossary GLOSSARY.tsv scan SOURCE.md

lookup: 용어(부분 일치, 대소문자 무시)를 조회해 역어와 노트를 출력
scan:   영어 원문에서 용어집에 등재된 용어를 모두 찾아 번역 전 참고표를 출력
"""

import argparse
import re
import sys
from pathlib import Path


def load(path):
    rows = []
    for line in Path(path).read_text(encoding="utf-8").splitlines()[1:]:
        cols = line.split("\t")
        if len(cols) >= 2 and cols[0].strip():
            rows.append((cols[0].strip(), cols[1].strip(), cols[2].strip() if len(cols) > 2 else ""))
    return rows


def cmd_lookup(rows, terms):
    for term in terms:
        hits = [r for r in rows if term.lower() in r[0].lower()]
        if not hits:
            print(f"'{term}': 용어집에 없음. 새 용어라면 등재 후 번역 (한-영 병기 검토)")
            continue
        for en, ko, note in hits:
            print(f"{en}\t{ko}" + (f"\t# {note}" if note else ""))


def cmd_scan(rows, source):
    text = Path(source).read_text(encoding="utf-8")
    # 코드블록(``` 또는 ~~~ 펜스)·내부 링크 문법 제거 후 산문만 검색
    text = re.sub(r"^(```|~~~).*?^\1", "", text, flags=re.S | re.M)
    text = re.sub(r"<info:[^>]*>", "", text)
    found = []
    for en, ko, note in rows:
        if not re.fullmatch(r"[A-Za-z][A-Za-z ().'/,-]*", en):
            continue
        n = len(re.findall(rf"(?<!\w){re.escape(en)}(?!\w)", text, re.IGNORECASE))
        if n:
            found.append((n, en, ko, note))
    found.sort(reverse=True)
    if not found:
        print("등재 용어가 발견되지 않았습니다.")
        return
    print(f"{'횟수':>4}\t용어\t역어\t노트")
    for n, en, ko, note in found:
        print(f"{n:>4}\t{en}\t{ko}\t{note}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--glossary", required=True)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("lookup")
    p1.add_argument("terms", nargs="+")
    p2 = sub.add_parser("scan")
    p2.add_argument("source")
    args = ap.parse_args()

    rows = load(args.glossary)
    if args.cmd == "lookup":
        cmd_lookup(rows, args.terms)
    else:
        cmd_scan(rows, args.source)


if __name__ == "__main__":
    main()
