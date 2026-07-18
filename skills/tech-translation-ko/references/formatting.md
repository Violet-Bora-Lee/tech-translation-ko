# Formatting · 문장부호·마크다운·코드 요소

Deterministic rules here are enforced by `scripts/check_translation.py` (rule IDs in
parentheses). This document explains the why and the edge cases the linter can't judge.

## Punctuation · 문장부호

- **문장 끝 쌍점 금지** (KO-E002). "다음 예제를 보세요." (○) / "다음 예제를 보세요:" (✕).
  예외: 리스트 항목의 굵은 라벨 뒤 쌍점("**시작 조건:** ...")은 라벨 구분자로 허용.
- **em-dash(—) 금지** (KO-E001). 원문의 dash 구조는 쉼표·마침표·괄호로 해체하거나
  문장을 다시 짠다.
- **강조는 작은따옴표, 인용은 큰따옴표**. 함수 실행이 잠시 '중단'되었다가(○).
  직접 대화·에러 문구 인용에만 큰따옴표를 쓴다(KO-W008).
- **짝 단어는 가운뎃점** (KO-E004). 대·소문자, 삽입·삭제 메서드. 슬래시(/)를 그대로
  두지 않는다. 가운뎃점이 어색하면 쉼표나 연결어로 푼다(resolve, reject를 호출함).
- **괄호와 마침표** (KO-E005). 괄호 안이 구이면 마침표는 밖: "업데이트하세요(안내서 참조)."
  괄호 안이 문장이면 안쪽: "입력합니다.(기호는 제거되었습니다.)" 혼합형 금지.
- **헤딩엔 마침표·느낌표를 붙이지 않는다** (KO-E003). 물음표는 실제 코퍼스 관행상
  허용된다('# 자바스크립트란?', '# 객체야 안녕?' 같은 제목이 실제로 쓰인다).
- **명사로 끝나는 문장엔 마침표를 찍지 않는다** (KO-W007). "텍스트 입력 시 이벤트 발생"
- **쉼표는 꼭 필요할 때만**. 원문의 쉼표를 그대로 옮기지 않는다. "예를 들어 `id`가 ..."
  ("예를 들어," ✕)
- 문장 끝 `:` 이나 문장 맨 앞 `...` 같은 영어식 문장부호는 최대한 한글화한다.

## Markdown structure · 마크다운 구조 보존

원문 병합·diff 추적이 필요한 프로젝트(ko.javascript.info 방식)에선 구조 보존이 필수 규칙이다.

- **줄 수를 원문과 동일하게 유지한다** (KO-E101). 문장을 나누더라도 같은 줄 안에서 나눈다.
- **코드블록 펜스 수·헤딩 수와 레벨·링크 URL을 원문과 일치시킨다** (KO-E102~104).
- 공백, 따옴표, 대시, 백틱 같은 특수문자는 수정하지 않는다. 자연어만 번역한다.
- 독립 문서 번역(구조 보존이 계약이 아닌 경우)이라면 줄 수 규칙은 완화해도 되지만
  헤딩·코드블록·링크 구조는 여전히 보존한다.

## Headings · 헤딩 재작성

구조는 보존하되 문구는 재창작 대상이다.

- 원문의 '용어: 설명' 쌍점 헤딩은 동작 중심으로 다시 쓴다.
  "innerHTML: the contents" → "innerHTML로 내용 조작하기"
- 제목은 개념어 직역보다 실제 다루는 내용으로. "Generators, advanced iteration" →
  "제너레이터와 비동기 이터레이션" (챕터가 실제로 다루는 주제로 특정)

## Code blocks · 코드 요소

코드는 '식별자·구문'과 '자연어'로 나눠 다르게 처리한다.

- **주석은 자연어다. 번역하고, 직역 대신 의도를 설명한다.**
  `// this alert shows first` → `// 얼럿 창이 가장 먼저 뜹니다.`
  `// 20 lines of code working with elem` → `// 매개변수로 받아온 elem을 이용한 코드`
  (분량 정보보다 코드의 의도를 전달)
- **사용자에게 보이는 문자열은 번역한다.** `alert("promise done!")` → `alert("프라미스 성공!")`,
  `prompt("Which module to load?")` → `prompt("어떤 모듈을 불러오고 싶으세요?")`
- **에러 메시지는 번역하지 않는다.** `// Error: this is not defined` 유지.
  본문에서 언급할 땐 '정의되지 않았다(not defined)'처럼 한-영 병기.
- **식별자·키워드·CSS 값은 절대 건드리지 않는다.** 변수명, 함수명, HTML 속성,
  색상 span(`<span style="color:...">`)의 마크업은 유지하고 감싼 텍스트만 번역.
- **예시 속 고유명사는 현지화할 수 있다.** "Winnie-the-Pooh" → "이보라"(번역자 이름),
  인명 John → 보라 등. 개념 전달과 무관한 문화 레퍼런스는 한국 독자에게 친숙한 것으로
  바꾸되, 본문 설명과 코드 출력이 일치하도록 함께 바꾼다.

## Special blocks · smart/warn/quote 블록

- ` ```smart header="..." ` 류의 **header 속성값도 번역 대상**이다.
  `header="console.dir(elem) versus console.log(elem)"` → `header="...의 차이"`
- 반어·유머 헤더는 직역하지 않고 한국어 관습으로 재창작한다.
  `header="Irony detected"` → `header="방금 들어온 속보입니다!"`
- 인용(quote) 블록의 격언은 직역 대신 같은 기능을 하는 격언으로 대체할 수 있다
  (도덕경 인용 → '어두운 방에서 검은 고양이 찾기' 격언, author 속성까지 교체).
  단 이는 튜토리얼처럼 어조가 자산인 글에서의 재량이다. 명세·API 문서에선 직역한다.

## Captions and images · 캡션·이미지

- 이미지 캡션의 명사구+쌍점 라벨은 완결 문장으로 바꾼다.
  "For instance, two points curve:" → "조절점이 두 개인 베지어 곡선을 살펴봅시다."
- 콘솔·UI에 실제로 뜨는 문구를 언급할 땐 화면과 일치하는 원문을 병기한다.
  화면에 안 뜨는 표현으로 의역하면 독자가 대조할 수 없다.

## Verification loop · 검증 루프

번역 후 반드시 실행한다.

```bash
python3 scripts/check_translation.py translated.md --source original.md --glossary glossary.tsv
```

error는 전부 수정하고, warning은 문맥을 보고 판단한다. 한국어 맞춤법 검사기
(부산대 검사기 등)를 마지막에 한 번 돌린다.
