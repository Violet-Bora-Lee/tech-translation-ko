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
   3. TTA 정보통신용어사전(terms.tta.or.kr). 한·영 병기 공식 사전으로 양자·보안·AI·
      클라우드 등 최신 분야까지 수록. 개별 조회용이며 저작권상 대량 수집은 금지
   4. 마이크로소프트 Language Portal Terminology Search
   5. 국립국어원 외래어 표기법 용례(음차 표기 결정: 스로틀·섬네일·다이내믹·아키텍처)와
      다듬은 말 목록(공공누리. 단 순화어라 업계 통용 표기와 다를 수 있음)
   6. 한글라이즈(위에 없을 때 음차 표기)

   최신 분야 참조처 상세와 라이선스 조건은 이 저장소
   `docs/analysis/research_glossary_sources.md` 참고.
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

**병기는 본문에서 한다. 헤딩에는 넣지 않는다.** 첫 등장이 헤딩이면 헤딩은 한글만
쓰고(`# 마이크로태스크`), 본문 첫 등장에 병기한다. 실제 교정 커밋에서 헤딩의 병기를
일괄 제거한 관행(`# 객체(object)` → `# 객체`)을 따른다.

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

## Deviating from the glossary · 용어집 이탈 판단

등재 역어가 문맥에서 어색할 때의 판단 기준이다.

- **합성어·도메인이 다르면 이탈이 아니다.** task=과제는 튜토리얼의 '연습 문제' 문맥이다.
  비동기 문맥의 task 단독은 '작업·태스크', microtask·macrotask는 음차 합성어
  '마이크로태스크·매크로태스크'로 쓴다. 등재 역어의 적용 범위(note)를 먼저 확인한다.
- **의도적으로 이탈하면 기록한다.** 어색해서 다른 역어를 썼다면 용어집 note에 문맥
  조건을 추가하거나, 수정 권한이 없는 상황(read-only 용어집)이면 번역 결과물에
  옮긴이 주나 별도 결정 로그로 남긴다. 조용한 이탈이 가장 나쁘다.
- 일회성 번역이라 공유 용어집을 고칠 수 없으면 '등재 후 번역' 절차는 '결정 기록 후
  번역'으로 대체한다.

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
남긴다. 이 저장소의 `docs/analysis/glossary.tsv`가 JS 도메인 실물 예시고, AI·양자·ICT
용어는 `docs/analysis/glossary-extended.tsv`에 출처 태그와 함께 분리되어 있다(용어↔표기
대응 쌍만 수록, 설명은 출처 라이선스 확인 전이라 미포함). 다른 도메인을 번역할 땐 같은
형식으로 프로젝트 용어집을 만들어 `--glossary`로 린터에 연결한다.
