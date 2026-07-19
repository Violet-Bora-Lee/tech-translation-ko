---
name: it-docs-translation-ko
description: Translate any English IT document into natural, publication-quality Korean — developer docs, READMEs, API references, release notes, UI strings, tech blog posts. Domain-neutral generalization of tech-translation-ko; bring your own glossary. Use for English-to-Korean technical translation or for reviewing/editing an existing one.
---

# it-docs-translation-ko

Translate English IT documents into Korean that reads like it was written in Korean
by a skilled technical author — no translationese, no meaning loss. This is the
domain-neutral sibling of `tech-translation-ko`: same techniques, no
javascript.info-specific contracts, house style, or glossary.

## Scope · 적용 범위

개발자 문서 전반에 쓴다. 튜토리얼, README, API 레퍼런스, 릴리스 노트, 매뉴얼,
기술 블로그, UI 문자열. 문서 장르에 따라 어조 다이얼을 조절한다
(`references/principles.md`) — 튜토리얼은 강연하듯, 레퍼런스·명세는 간결·정확하게.

## Workflow

1. **Read the whole source first.** Understand the document's genre — tutorials get
   a warmer, lecture-like tone; references and specs stay terse. See
   `references/principles.md`.
2. **Set up the project glossary, then scan.** 용어집은 프로젝트마다 다르다.
   기존 용어집이 있으면 그것을 쓰고, 없으면 `en<TAB>ko<TAB>note` TSV를 새로 만든다.
   ```bash
   python3 scripts/glossary_lookup.py --glossary <glossary.tsv> scan original.md
   ```
   For unregistered terms, follow the decision process in
   `references/terminology.md` (published books > official Korean docs > TTA >
   MS Terminology > 국립국어원 외래어 표기법), then register the decision.
3. **Decide the structural contract.** 원문 저장소와 diff 동기화가 필요한 프로젝트만
   '줄 수 = 원문 줄 수' 계약을 적용한다(`--source`로 린터가 검사). 독립 문서라면
   줄 수는 자유지만 헤딩·코드블록·링크 구조는 여전히 보존한다.
4. **Translate** applying, in priority order: meaning preservation > terminology
   consistency > structural contract (if adopted) > natural Korean. The core
   techniques are in `references/sentence-patterns.md` — read it before your first
   translation in a session. Formatting and code-element rules are in
   `references/formatting.md`; UI·매뉴얼 번역은 `references/kigo-conventions.md`의
   소프트웨어 현지화 절을 함께 본다.
5. **Lint the result and fix.**
   ```bash
   python3 scripts/check_translation.py translated.md [--source original.md] --glossary <glossary.tsv>
   ```
   Fix every `error`. Judge each `warning` in context. Re-run until clean.
6. **Self-review** with `references/review-checklist.md`.
7. **Final spell check — required, but always manual.** Run 나라 맞춤법 검사기(바른한글,
   https://nara-speller.co.kr/speller/ ) as the last pass — real correction corpora
   show spelling slips survive every earlier step, so do not skip this. However, the
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

## Project-specific decisions · 프로젝트별 결정 사항

범용 스킬이라 정답을 정하지 않는 항목이다. 프로젝트 시작 시 결정하고 기록한다.

- **구조 계약**: 줄 수 보존을 계약으로 삼을지(원문 diff 동기화 프로젝트) 여부
- **예시 현지화 수위**: 인명·문화 레퍼런스를 한국식으로 바꿀지. 튜토리얼처럼 어조가
  자산인 글은 현지화가 통하지만, 공식 문서·API 레퍼런스는 원문 유지가 기본이다
- **하우스 스타일**: 예제 에러 문자열 처리, 역주 형식, 고정 문구 치환 규칙 등.
  결정하면 용어집 note나 프로젝트 문서에 남긴다

## References

| File | When to read |
|---|---|
| `references/principles.md` | 우선순위·장르 판단이 필요할 때, 세션 시작 시 |
| `references/sentence-patterns.md` | 번역 시작 전 필독. 문장 변환 기법 11종 |
| `references/terminology.md` | 용어 결정·병기·음차 판단 |
| `references/formatting.md` | 문장부호·마크다운·코드 요소 처리 |
| `references/review-checklist.md` | 번역 후 자기 검수 |
| `references/examples.md` | 패턴이 감이 안 올 때 실제 대조 사례 |
| `references/kigo-conventions.md` | 시제·조사·외래어 표기 세칙·숫자·UI 현지화(KIGO 표준) |

## Scripts

Both scripts are stdlib-only Python 3.8+ and identical to the copies in
`tech-translation-ko` (keep them in sync when updating either skill).

- `scripts/check_translation.py` — deterministic lint. `error` (must fix: punctuation,
  markdown structure vs source) and `warning` (review: double passive, translationese,
  glossary deviations). `--source` enables the structural-contract checks; omit it for
  standalone documents. Supports `--format json` for programmatic use.
- `scripts/glossary_lookup.py` — `lookup <term>` and `scan <file>` over a TSV glossary
  (`en<TAB>ko<TAB>note`). This skill ships no default glossary — bring your project's
  own TSV. The repository's `docs/analysis/` has two starters you may reuse:
  `glossary.tsv` (JavaScript domain, with decision notes) and `glossary-extended.tsv`
  (AI·quantum·ICT pairs, source-tagged). Concatenate files if you want both.

## Provenance · 근거

이 스킬의 기법은 ko.javascript.info 번역 코퍼스 전수 분석(문서 76편 문단 대조,
교정 커밋 135건 코딩)과 KIGO 표준 스타일 가이드에서 추출했다. javascript.info에
번역 기여를 한다면 이 스킬 대신 하우스 스타일과 전용 용어집이 포함된
`tech-translation-ko`를 쓴다.
