---
name: tech-translation-ko
description: Translate English technical documentation into natural, publication-quality Korean. Use when translating docs, tutorials, READMEs, or API references from English to Korean, or when reviewing/editing an existing English-to-Korean technical translation. Distilled from the ko.javascript.info translation project.
---

# tech-translation-ko

Translate English technical documents into Korean that reads like it was written in
Korean by a skilled technical author — no translationese, no meaning loss.

## Workflow

1. **Read the whole source first.** Understand the document's genre (tutorial /
   reference / README) — tutorials get a warmer, lecture-like tone; references stay
   terse. See `references/principles.md`.
2. **Scan terminology before translating.**
   ```bash
   python3 scripts/glossary_lookup.py --glossary <glossary.tsv> scan original.md
   ```
   Use registered equivalents verbatim. For unregistered terms, follow the decision
   process in `references/terminology.md` (published books > MDN > MS Terminology >
   국립국어원 외래어 표기법), then register the decision.
3. **Translate** applying, in priority order: meaning preservation > terminology
   consistency > structural contract (line/markdown preservation if required) >
   natural Korean. The core techniques are in `references/sentence-patterns.md` —
   read it before your first translation in a session. Formatting and code-element
   rules are in `references/formatting.md`.
4. **Lint the result and fix.**
   ```bash
   python3 scripts/check_translation.py translated.md --source original.md --glossary <glossary.tsv>
   ```
   Fix every `error`. Judge each `warning` in context. Re-run until clean.
5. **Self-review** with `references/review-checklist.md`.
6. **Final spell check — required, but always manual.** Run 나라 맞춤법 검사기(바른한글,
   https://nara-speller.co.kr/speller/ ) as the last pass — the real correction corpus
   shows spelling slips survive every earlier step, so do not skip this. However, the
   service is run free of charge by a university lab and is vulnerable to bot traffic:
   **never call it automatically** from the translation loop, CI, or scheduled jobs.
   Run it once per document, by hand (or with the user explicitly initiating it), with
   throttled requests. `scripts/nara_speller.py` prepares chunks and parses results;
   the actual API call must happen in a real browser session. See the script docstring.
   If 바른한글 is down, fall back to the Daum grammar checker with
   `python3 scripts/nara_speller.py daum translated.md` (direct call, same manual-only
   etiquette).

## Non-negotiable rules · 즉시 적용 규칙

- 본문은 합니다체. we/you 등 인칭대명사는 번역하지 않는다. it/this는 지시 대상을 명시한다.
- 문장 끝 쌍점 금지, em-dash 금지, 강조는 작은따옴표, 짝 단어는 가운뎃점(대·소문자).
- 새 키워드 첫 등장은 한-영 병기: 프로퍼티(property), 브라우저 객체 모델(Browser Object Model, BOM).
- 코드에서: 주석·UI 문자열은 번역, 식별자·API·에러 메시지는 원문 유지.
- 긴 복문은 짧은 문장으로 분해하고 문장 사이 인과·대조를 접속어로 명시한다.
- 의미 누락 금지. 단어-단어 정확성보다 '오역 없음 + 번역투 없음'이 기준이다.

## References

| File | When to read |
|---|---|
| `references/principles.md` | 우선순위·장르 판단이 필요할 때, 세션 시작 시 |
| `references/sentence-patterns.md` | 번역 시작 전 필독. 문장 변환 기법 10종 |
| `references/terminology.md` | 용어 결정·병기·음차 판단 |
| `references/formatting.md` | 문장부호·마크다운·코드 요소 처리 |
| `references/review-checklist.md` | 번역 후 자기 검수 |
| `references/examples.md` | 패턴이 감이 안 올 때 실제 대조 사례 |
| `references/kigo-conventions.md` | 시제·조사·외래어 표기 세칙·숫자·UI 현지화(KIGO 표준) |

## Scripts

Both scripts are stdlib-only Python 3.8+.

- `scripts/check_translation.py` — deterministic lint. `error` (must fix: punctuation,
  markdown structure vs source) and `warning` (review: double passive, translationese,
  glossary deviations). Supports `--format json` for programmatic use.
- `scripts/glossary_lookup.py` — `lookup <term>` and `scan <file>` over a TSV glossary
  (`en<TAB>ko<TAB>note`). This repository ships two glossaries in `docs/analysis/`:
  `glossary.tsv` (JavaScript-domain, ~520 terms with decision notes) and
  `glossary-extended.tsv` (AI·quantum·ICT term-translation pairs, 245 entries,
  source-tagged only — see the license note in that file's README section). Bring
  your own TSV for other domains; concatenate files if you want both.
