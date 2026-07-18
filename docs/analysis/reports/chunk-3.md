# 청크 3 en↔ko 대조 분석 보고서

## 개요

- 분석 파일 수: 16개 (article 4, solution 2, task 4, index 6)
- 대상 범위: `2-ui` 대부분 + `5-network`/`7-animation` 섹션 index
- 분석 방향: 코드북 우선순위에 따라 기계적으로 규칙화하기 어려운 암묵지(A/B/G/H/I)를 상세 기록하고, 이미 wiki에 명문화된 규칙(C/E/F 등)은 빈도만 집계했다.

## 카테고리별 관찰 빈도

| ID | 카테고리 | 관찰 빈도 | 성격 |
|----|----------|-----------|------|
| A | 문장 분해·재구성 | 다수(약 20+) | 암묵지 |
| B | 어순·정보구조 재배치 | 6 | 암묵지 |
| C | 인칭·대명사 처리 | 다수(거의 전 문단) | wiki 명문 |
| D | 어휘 선택·용어 | 다수(약 15+) | 혼합 |
| E | 어미·문체 | 다수(전 문단) | wiki 명문 |
| F | 문장부호·표기 | 다수(약 25+) | wiki 명문 |
| G | 코드 요소 처리 | 9 | 암묵지 |
| H | 생략·보강 | 11 | 암묵지 |
| I | 담화 연결 | 8 | 암묵지 |
| J | 신규 패턴 | 3 | 신규 |

빈도가 '다수'인 카테고리는 거의 모든 문단에서 반복되는 wiki 명문 규칙이라 개별 엔트리 대신 대표 사례 1개와 총평만 기록한다.

---

## A. 문장 분해·재구성

### [A] 한 문장에 묶인 정의를 '역할 서술 + 부연' 두 문장으로 분해
- 원문: `The Document Object Model, or DOM for short, represents all page content as objects that can be modified.`
- 번역: `문서 객체 모델(Document Object Model, DOM)은 웹 페이지 내의 모든 콘텐츠를 객체로 나타내줍니다. 이 객체는 수정 가능합니다.`
- 위치: 2-ui/1-document/01-browser-environment/article.md:39
- 설명: 관계절 `that can be modified`를 뒤에 독립 문장('이 객체는 수정 가능합니다')으로 떼어냈다. 영어의 후치 수식을 한국어에서 짧은 단문 두 개로 나눠 가독성을 높이는 대표 기법이다. 같은 파일 5행에서도 "A platform may be ... coffee machine" 한 문장을 '호스트라고 불립니다 / 호스트는 ~가 될 수도 있습니다' 두 문장으로 분해했다.

### [A] 평서문을 청유·권유 문장으로 전환
- 원문: `Let's start with an example.`
- 번역: `먼저 예시부터 살펴봅시다.`
- 위치: 2-ui/2-events/02-bubbling-and-capturing/article.md:3
- 설명: 영어 명령형 도입("Let's ...")을 한국어 청유형('~봅시다')으로 옮긴다. 리듬 어미 '-죠'(browser-environment:7 "제공해주죠")와 함께 문어체 강의 톤을 만든다. 빈도 다수.

### [A] 열거 항목을 완결 서술문으로 확장
- 원문: `1. On that <p>. / 2. Then on the outer <div>.`
- 번역: `1. <p>에 할당된 onclick 핸들러가 동작합니다. / 2. 바깥의 <div>에 할당된 핸들러가 동작합니다.`
- 위치: 2-ui/2-events/02-bubbling-and-capturing/article.md:39
- 설명: 영어의 명사구 나열("On that <p>")을 매 항목 주어·서술어를 갖춘 완전한 문장으로 풀었다. 생략된 동사(runs onclick)를 각 항목에 반복 복원해 독립적으로 읽히게 한다. Viki 패턴 2(지시어·압축 풀어쓰기)와 동일 방향.

---

## B. 어순·정보구조 재배치

### [B] 2단계 리스트를 타깃 단계를 분리한 3단계로 재배치 (가장 주목할 사례)
- 원문:
  ```
  1. HTML -> BODY -> FORM -> DIV -> P (capturing phase, the first listener):
  2. P -> DIV -> FORM -> BODY -> HTML (bubbling phase, the second listener).
  Please note, the P shows up twice, because we've set two listeners...
  ```
- 번역:
  ```
  1. HTML -> BODY -> FORM -> DIV (캡처링 단계, 첫 번째 리스너)
  2. P (타깃 단계, 캡쳐링과 버블링 둘 다에 리스너를 설정했기 때문에 두 번 호출됩니다.)
  3. DIV -> FORM -> BODY -> HTML (버블링 단계, 두 번째 리스너)
  ```
- 위치: 2-ui/2-events/02-bubbling-and-capturing/article.md:183
- 설명: 영어는 캡처링/버블링 2단계로 묶고 `P`의 중복을 아래 별도 문장으로 설명했다. 번역자는 `P`(타깃 단계)를 독립된 2번 항목으로 끌어올리고 중복 설명을 항목 안 괄호로 흡수했다. 원문의 정보를 재배치해 리스트 자체가 '캡처링→타깃→버블링' 3단계 구조를 시각적으로 드러내도록 재구성한 것으로, 문장 단위가 아닌 정보 블록 단위 변환의 대표 사례다.

### [B] 정의문의 어순 도치 — 결론(용어)을 술부로 이동
- 원문: `A host environment provides its own objects and functions in addition to the language core.`
- 번역: `호스트 환경은 랭귀지 코어(ECMAScript - 옮긴이)에 더하여 플랫폼에 특정되는 객체와 함수를 제공합니다.`
- 위치: 2-ui/1-document/01-browser-environment/article.md:7
- 설명: `in addition to the language core`(문장 끝 부사구)를 한국어에서 목적어 앞('~에 더하여')으로 당겨 한국어 정보 흐름(수식어 선행)에 맞췄다.

### [B] 도입 문단을 '개괄 종료 선언'으로 재구성
- 원문: `Let's see more details of them.`
- 번역: `개괄적인 설명은 여기서 마치고 이제 submit 이벤트와 메서드에 대해 자세히 살펴봅시다.`
- 위치: 2-ui/4-forms-controls/4-forms-submit/article.md:7
- 설명: 짧은 전환 문장을 '앞 내용은 개괄이었다'는 메타 정보를 보강해 확장했다. 독자에게 문서 구조상 위치를 알려주는 담화 표지 역할(H 보강 겸함).

---

## C. 인칭·대명사 처리 (wiki 명문 — 빈도만)

- 대표: `We can change or create anything` → `document 객체를 이용해 페이지 내 그 무엇이든 변경할 수 있고`(browser-environment:41). 주어 'We'를 생략하고 지시어 'it'을 가리키는 대상('document 객체')으로 명시.
- 빈도: 거의 모든 문단. we/you 생략은 예외 없이 적용되며, `it`/`this`를 지시 대상 명사로 풀어쓰는 사례가 특히 잦다(예: bubbling:64 `it doesn't change` → '버블링이 진행되어도 변하지 않습니다'로 주어 복원).

## D. 어휘 선택·용어

### [D] 한-영 병기 후 이후 등장에선 한글만
- 대표: `host` 첫 등장 시 '호스트(host)'로 병기(browser-environment:5), 이후 문단에선 '호스트'만 사용.
- 빈도: 약 15회. 개념어 첫 등장에만 괄호 병기하는 규칙이 일관됨. Viki 패턴 8과 일치.

### [D] 관용 표현의 의역
- 원문: `Yes, you heard that right.`
- 번역: (삭제, 다음 문장에 흡수)
- 위치: 2-ui/1-document/01-browser-environment/article.md:89
- 설명: 영어 구어 삽입구를 그대로 옮기지 않고 생략했다. 반대로 `The outdated event.which` 헤딩은 '역사의 뒤안길로 사라진 event.which'(mouse-events:71)로 관용구를 살려 의역했다 — 문맥에 따라 삭제/윤색을 선택.

### [D] 유의어 교체로 단조로움 회피
- 원문: `provides ... provides ...` (반복)
- 번역: '제공하고 ... 제공해주죠'(browser-environment:7)
- 설명: 같은 동사 반복 시 어미 변화('-하고'/'-해주죠')로 리듬을 준다.

## E. 어미·문체 (wiki 명문 — 빈도만)

- 합니다체 전면 적용, '-죠'/'-네요'(forms-submit:34 "좀 이상해 보이긴 하네요") 리듬 어미, 청유형 '~봅시다'/'~살펴봅시다' 다수.
- '-시-' 존칭은 독자 지시문에 제한적으로 사용('살펴보세요', '확인해보시길 바랍니다').
- 빈도: 전 문단.

## F. 문장부호·표기 (wiki 명문 — 빈도만)

- 쌍점 제거: 영어 `For instance:` → '예시:' 또는 '예시를 살펴봅시다'로 전환. smart 헤딩 끝 문장부호 제거.
- 큰따옴표→작은따옴표: `"root" object` → "'루트' 객체"(browser-environment:13), `"target"` → "'타깃'"(bubbling:60). 강조는 작은따옴표로 통일. 빈도 약 20회.
- 가운뎃점: `mousedown/mouseup` → `mousedown·mouseup`(mouse-events:11), `Windows/Linux/Mac` → 'Windows, Linux, Mac'. 슬래시를 가운뎃점·쉼표로 치환. 빈도 5회.
- 명사 종결 무마침표: 요약 리스트 항목('버튼 관련: button')에서 명사 종결 시 마침표 생략.

## G. 코드 요소 처리

### [G] 코드 블록 내 주석 전면 번역
- 원문: `// global functions are methods of the global object:`
- 번역: `// 전역 함수는 전역 객체(window)의 메서드임`
- 위치: 2-ui/1-document/01-browser-environment/article.md:25
- 설명: 코드 주석을 번역하면서 원문에 없던 '(window)'를 보강해 어떤 전역 객체인지 명시했다. 또한 문장 끝 쌍점을 제거하고 명사형('~메서드임')으로 종결 — 산문과 다른 주석용 축약 어미를 적용한 점이 특징. 코드 주석 번역은 총 9개 파일에서 관찰.

### [G] UI 문자열·데모 텍스트 번역, 단 식별자·API는 원문 유지
- 원문: `alert("Hello");` / `value="Click me..."` / `form.innerHTML = '<input name="q" value="test">'`
- 번역: `alert("안녕하세요.");` / `value="마우스 왼쪽이나 오른쪽 버튼을 사용해 클릭해보세요."` / `value="테스트"`
- 위치: browser-environment:22, mouse-events:46, forms-submit:59
- 설명: 사용자에게 보이는 문자열 리터럴·버튼 라벨은 번역하되 `name="q"`, 프로퍼티명, 메서드명은 원문 유지. 번역 대상과 비대상의 경계가 'UI에 노출되는 자연어냐'로 일관되게 그어진다.

### [G] 데모 콘텐츠를 로컬라이즈 목적으로 통째 교체
- 원문: `Dear user, The copying is forbidden for you. If you know JS or HTML, then you can get everything from the page source though.`
- 번역: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...`
- 위치: 2-ui/3-event-details/1-mouse-events-basics/article.md:189
- 설명: oncopy 데모의 본문을 번역하지 않고 Lorem ipsum 더미 텍스트로 교체했다. 복사 방지 데모라 실제 문구 의미가 중요하지 않다고 판단해 번역 대신 플레이스홀더로 대체한 사례. 얼럿 메시지('불법 복제를 예방하기 복사 기능을 막아놓았습니다!')는 번역 유지 — 기능적으로 노출되는 문자열과 채우기용 텍스트를 구분해 처리했다.

### [G] smart 헤딩 내부 텍스트 번역 + 톤 보강
- 원문: `header="DOM is not only for browsers"`
- 번역: `header="DOM은 브라우저만을 위한 모델이 아닙니다."`
- 위치: browser-environment:54
- 설명: smart 블록 `header="..."` 속성값도 번역 대상. 명사구 제목을 완결 서술문으로 풀고 '모델'을 보강했다. 헤딩이지만 smart 박스 제목은 문장형 번역을 허용(일반 ## 헤딩의 무마침표 규칙과 구분).

## H. 생략·보강

### [H] '- 옮긴이' 주 삽입으로 배경지식 보강
- 원문: `A host environment provides its own objects and functions in addition to the language core.`
- 번역: `호스트 환경은 랭귀지 코어(ECMAScript - 옮긴이)에 더하여 ...`
- 위치: 2-ui/1-document/01-browser-environment/article.md:7
- 설명: '랭귀지 코어'가 구체적으로 ECMAScript임을 옮긴이 주로 명시했다. 원문 독자는 문맥으로 알지만 번역 독자를 위해 배경을 채워 넣는 대표적 보강 기법.

### [H] 독자 배려 문장·경험적 표현 추가
- 원문: `As you can see from the list above, a user action may trigger multiple events.`
- 번역: `위에서 소개한 마우스 이벤트를 보면서 눈치채셨겠지만, 사용자는 단 하나의 동작을 했어도 실행되는 이벤트는 여러 개일 수 있습니다.`
- 위치: 2-ui/3-event-details/1-mouse-events-basics/article.md:33
- 설명: 'as you can see'를 '눈치채셨겠지만'으로 옮기며 독자에게 말을 거는 톤을 강화하고, 'a user action'을 '사용자는 단 하나의 동작을 했어도'로 풀어 대비를 부각했다. 보강 11회 관찰.

### [H] 원문 강조를 번역이 추가 생성
- 원문: `Until now, we only talked about bubbling, because the capturing phase is rarely used.` (일반 문장)
- 번역: `**캡처링 단계를 이용해야 하는 경우는 흔치 않기 때문에, 이전까진 주로 버블링만 설명했습니다. 캡처링에 관한 코드를 발견하는 일은 거의 없을 겁니다.**` (볼드 + 문장 추가)
- 위치: 2-ui/2-events/02-bubbling-and-capturing/article.md:135
- 설명: 원문에 없던 볼드 강조를 부여하고 'In fact ... invisible for us' 다음 문단의 요지('캡처링 코드를 볼 일이 거의 없다')를 앞으로 당겨 한 문장 보강했다. 번역자가 정보 중요도를 재판단해 시각적 위계를 새로 만든 사례(J와 경계).

### [H] 원문 군더더기 생략
- 원문: `Isn't it a bit strange? Why does the handler on <div> run if the actual click was on <em>?`
- 번역: `이상하지 않나요? <em>을 클릭했는데 왜 <div>에 할당한 핸들러가 동작하는 걸까요?`
- 위치: bubbling:13
- 설명: 대체로 충실히 옮기되, browser-environment:89 `Yes, you heard that right.` 같은 잉여 구어체는 삭제. 원문 존중과 군더더기 제거의 균형.

## I. 담화 연결

### [I] 인과 접속어를 명시적으로 삽입
- 원문: `We already covered the difference between them in the chapter <info:coordinates>. In short, ...`
- 번역: `두 정보에 대한 차이는 <info:coordinates> 챕터에서 다룬 바 있습니다. 그럼에도 불구하고 두 좌표에 대해 요약하자면 다음과 같습니다.`
- 위치: 2-ui/3-event-details/1-mouse-events-basics/article.md:139
- 설명: `In short`를 단순 '요약하면'이 아니라 '그럼에도 불구하고 ... 요약하자면'으로 옮겨 앞 문장(이미 다뤘다)과의 대조 관계('그런데도 다시 정리한다')를 접속어로 드러냈다. Viki 패턴 19와 동일 방향. 담화 접속 보강 8회 관찰.

### [I] 이유절을 '~때문입니다' 독립 문장으로 후치
- 원문: `The process is called "bubbling", because events "bubble" from the inner element up through parents like a bubble in the water.`
- 번역: `이런 흐름을 '이벤트 버블링'이라고 부릅니다. 이벤트가 제일 깊은 곳에 있는 요소에서 시작해 부모 요소를 거슬러 올라가며 발생하는 모양이 마치 물속 거품(bubble)과 닮았기 때문입니다.`
- 위치: bubbling:48
- 설명: `because` 종속절을 끊어 '~때문입니다'로 끝나는 독립 문장으로 만들었다. 결과를 먼저 말하고 이유를 뒤에 붙이는 한국어 담화 흐름. A(문장 분해)와 결합된 빈출 패턴.

## J. 신규 패턴

### [J] task.md 미번역 — 원문 그대로 유지
- 원문/번역 동일: `# Show a note near the element` 이하 전문이 영어 원문과 100% 동일
- 위치: 2-ui/1-document/11-coordinates/2-position-at/task.md 전체
- 설명: 이 task 파일은 번역이 전혀 진행되지 않고 영어 원문이 그대로 있다. 줄 수 보존 규칙상 빈 번역이 원문으로 남은 상태로 추정된다. 청크 내 번역 커버리지가 100%가 아님을 보여주는 사례로, 패턴 추출 시 '미번역 파일' 필터링이 필요하다.

### [J] 번역 과정의 오탈자·오역 잔존
- 사례1: `찾교`(오타, '찾고') — find-elements/solution.md:33
- 사례2: `from을 정확히`(오타, 'form을') — find-elements/solution.md:24
- 사례3: clientX/Y와 pageX/Y의 설명이 서로 뒤바뀜 — mouse-events:141 ('클라이언트 좌표 ... 웹 문서를 기준으로', '`pageX`와 `pageY`는 창 왼쪽 위를 기준으로'는 원문과 반대)
- 설명: 번역 규칙 추출 목적에는 노이즈이지만, 골든 데이터 구축 시 이런 오류를 제외해야 하므로 기록한다. 특히 사례3은 의미 역전 오역이라 학습 데이터로 부적합.

### [J] index/섹션 요약의 능동적 확장
- 원문: `CSS and JavaScript animations.`
- 번역: `CSS와 자바스크립트를 사용해 애니메이션을 만드는 방법을 학습합니다.`
- 위치: 7-animation/index.md:3
- 설명: 명사구 한 줄 설명을 '~하는 방법을 학습합니다'라는 완결 문장으로 확장하는 패턴이 index 파일 전반에서 반복(2-ui/2-events/index.md, 2-ui/3-event-details/index.md 등). 섹션 표지 문구를 학습 안내문 톤으로 통일하는 관례.

---

## 종합 총평

청크 3의 번역자는 **문장 단위가 아니라 정보 블록 단위로 재구성**하는 경향이 뚜렷하다. 특히 리스트 구조 재배치(B, bubbling:183의 3단계 분리), 원문에 없는 강조·옮긴이 주 삽입(H), 인과·대조 접속어 명시(I)가 반복적으로 관찰된다. 코드 요소 처리(G)에서는 'UI에 노출되는 자연어는 번역, 식별자·API는 유지'라는 경계가 일관되며, 데모 더미 텍스트는 Lorem ipsum으로 교체하는 실용적 판단까지 나타난다. wiki 명문 규칙(C/E/F)은 예외 없이 적용되어 빈도 집계로 갈음했다. 학습 데이터 구축 시 position-at/task.md(미번역)와 오탈자·오역(J) 3건은 제외 대상이다.
