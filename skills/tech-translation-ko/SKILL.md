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
5. **Self-review** with `references/review-checklist.md`, then (if available) run a
   Korean spell checker as the final pass.

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

## Scripts

Both scripts are stdlib-only Python 3.8+.

- `scripts/check_translation.py` — deterministic lint. `error` (must fix: punctuation,
  markdown structure vs source) and `warning` (review: double passive, translationese,
  glossary deviations). Supports `--format json` for programmatic use.
- `scripts/glossary_lookup.py` — `lookup <term>` and `scan <file>` over a TSV glossary
  (`en<TAB>ko<TAB>note`). A 530-term JavaScript-domain glossary ships in
  `docs/analysis/glossary.tsv` of this repository; bring your own for other domains.
