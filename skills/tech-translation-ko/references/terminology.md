# Terminology · 용어 처리

How to decide Korean equivalents for English technical terms. Derived from the
ko.javascript.info glossary (530+ entries) and its recorded decision log.

## Decision process · 번역어 결정 절차

When you meet a term, resolve it in this order. 아래 순서로 판단한다.

1. **Check the project glossary first.** 프로젝트 용어집이 있으면 무조건 등재된 역어를 쓴다.
   공동 작업에선 번역어 통일이 정확성만큼 중요하다. `glossary_lookup.py`로 조회한다.
2. **If absent, consult authorities in this order.** 용어집에 없으면 아래 우선순위로 근거를 찾는다.
   1. 해당 분야의 출판된 번역서(예: JS라면 모던 자바스크립트 Deep Dive, 러닝 자바스크립트 등)
   2. MDN 한국어 문서 등 권위 있는 공식 문서 번역
   3. 마이크로소프트 Language Portal Terminology Search
   4. 국립국어원 외래어 표기법 용례(음차 표기 결정: 스로틀·섬네일·다이내믹·아키텍처)
   5. 한글라이즈(위에 없을 때 음차 표기)
3. **Register the decision.** 새 용어는 용어집에 등재하고 나서 번역한다. 번역어를 나중에
   바꾸면 '기존 X에서 Y로 변경'과 근거를 이력으로 남긴다.
4. **Reality overrides authority.** 근거 있는 역어라도 실제 문장에 넣어 보고 의미가 와닿지
   않으면 혼용을 허용한다(사례: custom → '사용자 지정'이 MS 근거였으나 실제 문장 적합성
   문제로 '커스텀'과 혼용 결정).

## Translate, transliterate, or keep? · 번역·음차·원문 유지 판단

- **Keep in English** (번역하지 않음):
  - 제품·회사·언어 이름: Chrome, Firefox, Windows, Mac, Ruby, Google
  - 코드 식별자로 기능하는 것: `null`, `undefined`, `true`/`false`, `resolve`/`reject`
    (함수 이름일 때), `document`/`window` (객체를 가리킬 때), `props`, `ref`, `Hook`
  - 정착된 역어가 없는 개념: assertion, iterator, dataset, falsy/truthy
    (첫 등장에서만 'falsy(거짓 같은 값)' 병기)
  - 에러 메시지: `// Error: this is not defined` 같은 주석 속 에러 내용은 번역하지 않는다
- **Transliterate** (음차): 업계에서 소리 나는 대로 통용되는 용어.
  콜백, 프라미스, 스코프, 렌더링, 폴리필, 트랜스파일. 표기는 국립국어원 외래어
  표기법 용례를 따른다('썸네일' 아닌 '섬네일', '쓰로틀' 아닌 '스로틀').
- **Translate** (번역): 안정된 한국어 역어가 있는 개념.
  함수, 객체, 변수, 반복문, 구조 분해 할당, 가비지 컬렉션, 동일 출처 정책.

원문 음만 따서 쓰는 동사는 '명사형 + ~하다'로 옮긴다. render → 렌더링하다(렌더하다 ✕),
bind → 바인딩하다.

## First-appearance annotation · 첫 등장 한-영 병기

새로 등장하는 키워드는 **한-영** 순서로 병기한다(영-한이 아니다).

- 프로퍼티(property)
- 브라우저 객체 모델(Browser Object Model, BOM)
- 먼저 들어온 작업을 먼저 실행합니다(FIFO, first-in-first-out)

약어는 약어를 앞에 두고 괄호에 풀이를 쓴다. 미국중재협회(AAA, American Arbitration
Association). 한글 풀이가 무의미하면 영문 풀이만 남긴다. 병기는 문서당 첫 등장
1회면 충분하고 이후엔 정해진 역어만 쓴다.

## Distinctions that matter · 자주 틀리는 구분

| 원어 | 역어 | 헷갈리는 상대 |
|---|---|---|
| property | 프로퍼티 | attribute = 속성 |
| argument | 인수 | parameter = 매개변수 |
| declaration | 선언 | definition = 정의 |
| expression | 표현식 | statement = 문·구문 |
| padding | 패딩 | margin = 마진 ('여백'으로 뭉개지 않는다) |
| spec (테스트 문서) | 스펙 | specification (명세 문서) = 명세(서) |

`type`은 단독이면 '타입', 합성어면 붙여서 'xx형'(문자형, 숫자형). 함수 이름을 지칭할 땐
'함수 Exit'처럼 함수를 앞에 두되, 범주를 나타내면 'async 함수, alert 함수'처럼 뒤에 둔다.

## Context-dependent terms · 문맥 의존 용어

같은 단어도 문맥에 따라 역어가 갈린다. 용어집 노트에 조건을 함께 기록한다.

- document: 일반 문서는 '문서', `document` 객체는 원문 유지
- state: 일반 문맥은 '상태', React 문맥은 state 유지
- local: 지역 변수는 '지역', local server는 '로컬'
- transition: 일반은 '전환', CSS transition은 '트랜지션'
- table: `<table>` 태그는 '테이블', 그 외 '표'와 혼용
- resolve: 함수명이면 원문, 처리 상태면 '이행되다'

## Synonym variation · 유의어 변주

1:1 고정 번역은 문장을 단조롭게 만든다. 가까운 곳에서 같은 단어가 반복되면 역어를
바꾼다. common → 일반적으로·널리·흔히, call/invoke → 호출하다·실행하다. 단, 용어집에
등재된 핵심 용어는 변주 대상이 아니다(프로퍼티를 '속성'으로 바꿔 부르면 안 된다).

## Glossary file format · 용어집 파일 형식

`glossary.tsv`는 `en<TAB>ko<TAB>note` 3열이다. note에 결정 근거·문맥 조건·병기 규칙을
남긴다. 이 저장소의 `docs/analysis/glossary.tsv`가 JS 도메인 실물 예시다. 다른 도메인을
번역할 땐 같은 형식으로 프로젝트 용어집을 만들어 `--glossary`로 린터에 연결한다.
