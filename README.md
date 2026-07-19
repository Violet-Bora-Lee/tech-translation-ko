# tech-translation-ko

**English-to-Korean technical documentation translation skill**, distilled from the
[ko.javascript.info](https://ko.javascript.info) translation project — one of the largest
and most carefully reviewed Korean technical translation efforts (400+ documents,
multi-reviewer workflow, a 500+ term glossary, and a written style guide).

영어 기술문서를 한국어로 번역할 때 쓰는 skill입니다. ko.javascript.info 번역 프로젝트를
이끈 번역자의 문서 76편(원문·번역 대조)과 교정 커밋 135건, 운영 용어집·스타일 가이드를
분석해 명문화된 규칙과 암묵지를 추출했습니다.

## Two skills · 두 가지 스킬

이 저장소는 같은 기법을 공유하는 스킬 두 개를 제공합니다.

| Skill | 용도 |
|---|---|
| `skills/tech-translation-ko` | **javascript.info 기여용.** 줄 수 보존 계약, JS 도메인 용어집, 하우스 스타일(예제 인명 현지화, 에러 문자열 치환 등)이 포함됩니다. |
| `skills/it-docs-translation-ko` | **범용 IT 문서 번역용.** README·API 레퍼런스·릴리스 노트·매뉴얼·기술 블로그 등 모든 영→한 IT 문서에 씁니다. 도메인 전용 계약·하우스 스타일을 걷어내고 용어집은 프로젝트별로 연결합니다(bring your own glossary). |

javascript.info에 기여한다면 전자를, 그 외 모든 번역엔 후자를 설치하세요.

## What's inside · 구성

```
skills/tech-translation-ko/        # javascript.info 특화 (아래 구조)
skills/it-docs-translation-ko/     # 범용판 (같은 구조, 도메인 중립 내용)
├── SKILL.md                  # Entry point — workflow and core principles
├── references/
│   ├── principles.md         # Translation philosophy and priorities
│   ├── sentence-patterns.md  # Sentence restructuring techniques (the tacit knowledge)
│   ├── terminology.md        # Terminology decision process + glossary format
│   ├── formatting.md         # Punctuation, markdown, code comments, captions
│   ├── review-checklist.md   # Review checklist from 135 correction commits
│   ├── examples.md           # Annotated before/after corpus (CC BY-NC excerpts)
│   └── kigo-conventions.md   # KIGO standard style guide summary (tense, particles, UI)
└── scripts/
    ├── check_translation.py  # Deterministic lint: punctuation, structure, glossary
    └── glossary_lookup.py    # Glossary lookup / source-term scan
```

The workflow is **translate → run the linter → fix violations → re-check**.
Deterministic rules are enforced by script; the LLM (or human) focuses on what
machines can't judge — sentence flow, naturalness, meaning preservation.

번역 → 스크립트 검사 → 위반 수정 → 재검사 순서로 진행합니다. 기계로 판별 가능한
규칙은 스크립트가 잡고, 문장 흐름·자연스러움·의미 보존은 LLM과 사람이 맡습니다.

## Install · 설치

### Claude Code

```bash
git clone https://github.com/Violet-Bora-Lee/tech-translation-ko

# General-purpose IT docs skill (recommended for most users)
cp -r tech-translation-ko/skills/it-docs-translation-ko ~/.claude/skills/

# javascript.info contribution skill
cp -r tech-translation-ko/skills/tech-translation-ko ~/.claude/skills/

# Or per-project: copy into .claude/skills/ instead
```

Then ask Claude to translate an English document to Korean — the skill activates
automatically, or invoke it explicitly with `/it-docs-translation-ko`
(or `/tech-translation-ko`).

### Any LLM · 범용 LLM

`SKILL.md`와 `references/` 문서는 도구 중립적인 마크다운입니다. 번역 프롬프트에
`SKILL.md`를 시스템 지침으로 넣고, 필요한 reference 문서를 함께 제공하면 됩니다.
린터는 Python 3.8+ 단독 실행 파일이라 어느 파이프라인에서든 쓸 수 있습니다.

```bash
python3 scripts/check_translation.py translated.md \
  --source original.md --glossary your-glossary.tsv
```

## Real-world case · 실전 사례

This skill has completed a full contribution cycle on the corpus it was distilled from:
[javascript-tutorial/ko.javascript.info#1899](https://github.com/javascript-tutorial/ko.javascript.info/pull/1899)
translated the untranslated *Server Sent Events* chapter (271 lines, line-count preserved).

skill로 미번역 챕터 '서버 전송 이벤트'를 번역해 실제 기여 PR까지 올린 사례입니다.
용어 스캔 → 번역 → 린터(0 error) → 로컬 서버 렌더링 확인 → 수기 퇴고 순서로
진행했고, 퇴고에서 나온 수정 패턴은 다시 skill에 반영됐습니다
(`references/sentence-patterns.md`의 '주체·방향·자동성' 패턴,
`docs/analysis/validation/user_edit_patterns.md`).

## Methodology · 방법론

The skill was built by mining the translation history, not by writing rules from
imagination. See `docs/analysis/` for the full reproducible pipeline:

- `build_manifest.py` — attributes every file in the corpus to its translator via
  git history and blame share
- `codebook.md` — the pattern taxonomy used by analysis agents
- `reports/` — raw pattern reports from parallel en↔ko comparison and
  correction-diff coding
- `glossary.tsv` — the 500+ term glossary with decision notes

명문화된 규칙(wiki·CONTRIBUTING·용어집)과 diff에서 발굴한 암묵지를 출처를 구분해
정리했습니다. 규칙과 실제 관행이 충돌하면 실제 코퍼스 관행을 따랐습니다.

## License

Code and documentation are MIT licensed. Example sentence pairs quoted from
javascript.info / ko.javascript.info are CC BY-NC by Ilya Kantor and contributors —
see `LICENSE` and per-file attribution notes.

**Glossary data**: `docs/analysis/glossary.tsv` (JavaScript domain) carries decision
notes from the ko.javascript.info project. `docs/analysis/glossary-extended.tsv`
(AI · quantum · ICT) contains only English↔Korean term-translation pairs with source
tags — factual correspondences extracted from published Korean references (2025 AI
핵심용어, TTA·전자신문 최신 ICT 시사용어 2025, TTA 정보통신용어사전). Definitions were
deliberately not reproduced. If you plan to redistribute the extended glossary at
scale, verify usage terms with the respective publishers first
(see `docs/analysis/research_glossary_sources.md`).
