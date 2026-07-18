# 청크 2 중복 분석 보고서 (일관성 검증용)

## 개요

- 분석 파일 수: 11개 (article 3, solution 2, task 1, index 5)
- 대상 청크: chunks.json 인덱스 2
- 성격: 다른 분석자와의 일관성 검증을 위한 독립 중복 분석 (타 보고서 미참조)

분석 대상 중 본문량이 많아 패턴이 집중된 파일은 `05-basic-dom-node-properties/article.md`, `11-async/07-microtask-queue/article.md`, `13-modules/03-modules-dynamic-imports/article.md`, `99-js-misc/04-reference-type/3-why-this/solution.md` 네 건이다. index.md 5개는 한두 문장짜리 챕터 표지라 패턴 표본이 얕다.

## 카테고리별 관찰 빈도

| 카테고리 | 관찰 빈도 | 비고 |
|---|---|---|
| A. 문장 분해·재구성 | 12 | 긴 나열 문장을 항목·짧은 문장으로 분해, 의문문→청유문 전환 |
| B. 어순·정보구조 재배치 | 8 | 열거 명시화("First,"→"첫 번째 제약은"), 헤딩 재구성 |
| C. 인칭·대명사 처리 | 20+ | we/you/it/this 생략이 거의 전 문단 |
| D. 어휘 선택·용어 | 14 | 한-영 병기, 약어 풀이, 유의어 교체 |
| E. 어미·문체 | 18 | 합니다체, '-죠/-네요' 리듬 어미, 청유형 |
| F. 문장부호·표기 | 10 | 헤딩 쌍점→동사구, 명사 종결, 헤딩 부호 제거 |
| G. 코드 요소 처리 | 11 | 주석 번역, 코드 문자열 현지화, smart header, IDL 주석 |
| H. 생략·보강 | 9 | 독자 배려 부연, 담화 마무리 문장 추가 |
| I. 담화 연결 | 10 | But→"그럼에도 불구하고", 인과 '~때문입니다' 명시 |
| J. 신규 패턴 | 3 | 코드 예제 문화적 현지화(번역자 이름 삽입) |

---

## 상세 패턴 (암묵지 우선)

### [J] 코드 예제 문자열을 번역자 자신의 이름·한국 문맥으로 현지화
- 원문: `let name = prompt("What's your name?", "<b>Winnie-the-Pooh!</b>");`
- 번역: `let name = prompt("이름을 알려주세요.", "<b>이보라</b>");`
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:400
- 설명: 서구권 문화 레퍼런스('곰돌이 푸')를 단순 음차하지 않고 번역자 본인 이름으로 교체했다. 본문 설명(407~408줄)의 출력 예시 `<b>이보라</b>`까지 일관되게 맞춰, 독자가 실행 결과를 즉시 대응시킬 수 있게 했다. 기계적 규칙화가 불가능한 재량적 현지화 판단이다.

### [H] 원문의 짧은 조건절을 독자 체감 서술로 확장 보강
- 원문: `In the chatDiv example above the line ... re-creates the HTML content and reloads smile.gif (hope it's cached). If chatDiv has a lot of other text and images, then the reload becomes clearly visible.`
- 번역: `...`smile.gif` 역시 다시 로딩되는 것이죠. 어딘가에 이런 리소스들을 캐싱해 놓았다면 좋았을 거라는 생각이 드는 순간이네요. `chatDiv`에 텍스트와 이미지가 많이 있었다면 내용을 다시 불러올 때 버벅임이 생기는걸 눈으로 확인하실 수 있을 겁니다.`
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:267
- 설명: 괄호 삽입구 `(hope it's cached)`를 독립 문장 '~생각이 드는 순간이네요'로 풀고, 'becomes clearly visible'을 '버벅임이 생기는걸 눈으로 확인하실 수 있을 겁니다'로 구체 감각화했다. 정보량은 유지하되 체감을 보강하는 재량 기법.

### [H] 원문에 없는 담화 마무리 문장 추가
- 원문: `...if any of them is in the "rejected" state, then the event triggers.`
- 번역: `...이 중 하나라도 '거부(rejected)' 상태이면 `unhandledrejection` 핸들러를 트리거 하죠. 이로써 앞선 의문이 자연스레 해결되었습니다.`
- 위치: 1-js/11-async/07-microtask-queue/article.md:100
- 설명: 원문에 없는 '이로써 앞선 의문이 자연스레 해결되었습니다'를 덧붙여, 98줄에서 던진 독자의 질문("왜 핸들러가 실행되지?")과 명시적으로 수미상관을 맺었다. 담화 완결성을 위한 보강.

### [A] 원문의 감탄·의문 연쇄를 청유형 결론으로 전환
- 원문: `That's strange, because the promise is definitely done from the beginning. Why did the .then trigger afterwards? What's going on?`
- 번역: `프라미스는 즉시 이행상태가 되었는데도 말이죠. 뭔가 이상하네요. 왜 `.then`이 나중에 트리거 되었을까요? 그 이유에 대해 알아봅시다.`
- 위치: 1-js/11-async/07-microtask-queue/article.md:20-22
- 설명: 정보구조를 재배치해 원인절('되었는데도 말이죠')을 앞세우고, 원문의 막연한 반문 'What's going on?'을 학습 유도형 '그 이유에 대해 알아봅시다'로 바꿔 다음 절과의 진행을 매끄럽게 했다.

### [B] 열거 신호어를 '제약'이라는 상위 개념으로 명시 재구성 + 과거형
- 원문: `First, we can't dynamically generate any parameters of import.` / `Second, we can't import conditionally or at run-time:`
- 번역: `첫 번째 제약은 `import`문에 동적 매개변수를 사용할 수 없다는 것이었습니다.` / `두 번째 제약은 런타임이나 조건부로 모듈을 불러올 수 없다는 점이었습니다.`
- 위치: 1-js/13-modules/03-modules-dynamic-imports/article.md:5, 13
- 설명: 부사 'First/Second'를 '첫 번째 제약은/두 번째 제약은'으로 명사화해 3줄의 '제약사항이 있죠'와 결속했다. 시제도 이미 설명이 끝난 정적 import를 회고하는 맥락이라 '~것이었습니다' 과거형으로 통일. 코드북 B의 열거 명시화 대표 사례.

### [I] 역접·전환 부사를 접속 표현으로 명시
- 원문: `But how can we import a module dynamically, on-demand?`
- 번역: `그럼에도 불구하고 모듈을 동적으로 불러와야 한다면 어떻게 해야 할까요?`
- 위치: 1-js/13-modules/03-modules-dynamic-imports/article.md:27
- 설명: 'But'을 '그럼에도 불구하고'로 풀어 앞 문단(제약이 필요한 이유)과의 대조를 분명히 했다. 유사 사례로 microtask:102 `But it does so later` → '다만 ~트리거 되므로'(인과 결합), basic-dom:9 'because ~ hierarchy' → '~때문에' 인과 명시가 있다.

### [A] 병렬 나열 원문을 근거절 포함 한 문장으로 통합·재구성
- 원문: `Different DOM nodes may have different properties. ... Text nodes are not the same as element nodes. But there are also common properties and methods between all of them, because all classes of DOM nodes form a single hierarchy.`
- 번역: `DOM 노드는 종류에 따라 각각 다른 프로퍼티를 지원합니다. ... 텍스트 노드는 요소 노드와 다른 프로퍼티를 지원하는 것은 말할 필요도 없습니다. 그런데 모든 DOM 노드는 공통 조상으로부터 만들어지기 때문에 노드 종류는 다르지만, 모든 DOM 노드는 공통된 프로퍼티와 메서드를 지원합니다.`
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:9
- 설명: 영어의 4문장 병렬을 재배치하며 'form a single hierarchy'라는 결과를 '공통 조상으로부터 만들어지기 때문에'라는 원인으로 앞당겨 배치했다. 'not the same' 강조는 '말할 필요도 없습니다' 관용구로 대응.

### [G] 코드 주석을 설명적으로 번역하고 코드 내 문자열도 현지화
- 원문: `alert("code finished"); // this alert shows first`
- 번역: `alert("코드 종료"); // 얼럿 창이 가장 먼저 뜹니다.`
- 위치: 1-js/11-async/07-microtask-queue/article.md:15
- 설명: 주석을 직역('이 얼럿이 먼저')하지 않고 '얼럿 창이 가장 먼저 뜹니다'로 서술화했다. 코드 문자열도 `"promise done!"`→`"프라미스 성공!"`, `"Hello"`→`"안녕하세요."` 등 실행 출력까지 번역. IDL 예제(80~114줄)의 주석 다수도 동일 방식. 총 11회 관찰.

### [F] 원문 헤딩의 쌍점 구조를 한국어 동사구로 재작성
- 원문: `innerHTML: the contents` / `outerHTML: full HTML of the element` / `nodeValue/data: text node content` / `textContent: pure text`
- 번역: `innerHTML로 내용 조작하기` / `outerHTML로 요소의 전체 HTML 보기` / `nodeValue/data로 텍스트 노드 내용 조작하기` / `textContent로 순수한 텍스트만`
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:199, 273, 326, 364
- 설명: 영어 헤딩의 '용어: 설명' 쌍점 패턴을 버리고 '~로 ~하기' 동작 중심 제목으로 전환했다. 문서 대제목도 `Node properties: type, tag and contents`→`주요 노드 프로퍼티`로 간결화. 헤딩 문장부호 금지 규칙과 결합.

### [D] 전문 용어·약어의 한-영 병기와 풀이
- 원문: `The queue is first-in-first-out` / `an "abstract" class` / `unused exports can be removed ("tree-shaken")`
- 번역: `먼저 들어온 작업을 먼저 실행합니다(FIFO, first-in-first-out)` / `'추상(abstract)' 클래스` / `사용하지 않는 모듈은 제거(가지치기)해야 하는데`
- 위치: 1-js/11-async/07-microtask-queue/article.md:30, 1-js/13-modules/03-modules-dynamic-imports/article.md:25
- 설명: 처음 등장하는 개념어는 한글 뒤 괄호로 원어를 병기하고, 'tree-shaken' 같은 비유 용어는 '가지치기'로 의역 병기했다. 'microtask queue(microtask queue)'는 V8 용어임을 본문에서 부연. 약어 풀이 규칙과 일치.

### [E] '-죠/-네요' 리듬 어미와 청유형으로 강연 톤 부여
- 원문: `Yeah, sounds strange, and strange it is, that's why we make a separate note about it here. Take a look.`
- 번역: `네, 뭔가 이상하게 들리실 겁니다. 실제로도 이상하고요. 그럴 것을 예상하고 구체적인 예시를 준비해 놓았습니다. 코드를 보며 이해해 봅시다.`
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:289
- 설명: 한 문장을 짧게 분해하며 '-고요' 구어체와 '이해해 봅시다' 청유형을 섞어 저자의 대화체를 살렸다. '등장했네요'(why-this:8), '말이죠'(microtask:20) 등 리듬 어미가 문서 전반에 분포. 총 18회 관찰.

### [C] we/you/it 인칭대명사 대량 생략
- 원문: `To explain the behavior of (3) and (4) we need to recall that property accessors ... return a value of the Reference Type.`
- 번역: `(3)과 (4)에서 어떤 일이 일어나는지 알려면 참조 타입을 다시 상기해야 합니다. 점이나 대괄호를 통해 프로퍼티에 접근하려는 경우 참조 타입 값(`(base, name, strict)`)이 반환됩니다.`
- 위치: 1-js/99-js-misc/04-reference-type/3-why-this/solution.md:19
- 설명: 'we need to'의 주어를 생략하고 한 문장을 둘로 분해했다. wiki 명문 규칙(인칭대명사 생략)과 일치하는 사례로 거의 전 문단에서 관찰(20건 이상), 빈도만 계수.

### [H] 원문 중복 표현을 정리하며 부연 삽입 (혼합)
- 원문: `These two are almost the same for practical use, there are only minor specification differences. So we'll use data, because it's shorter.`
- 번역: `이 두 프로퍼티는 아주 유사하고, 실무에서도 구분 없이 쓰긴 하지만 명세서상에 작은 차이가 있긴 합니다만 `data`가 좀 더 짧기 때문에 여기선 `data`를 사용하겠습니다.`
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:330
- 설명: '실무에서도 구분 없이 쓰긴 하지만'을 보강해 실용 맥락을 더했다. 다만 '~있긴 합니다만 ~때문에'로 양보절이 겹쳐 한 문장이 다소 길어진, 재구성이 덜 정제된 사례이기도 하다.

---

## 일관성 검증 노트

이 청크의 번역은 wiki 명문 규칙(쌍점 제거, 인칭대명사 생략, 헤딩 부호 제거, 합니다체)을 예외 없이 준수한다. 규칙화하기 어려운 재량 기법의 핵심은 세 축이다. (1) 열거·역접 신호어를 상위 개념('제약')과 접속 표현('그럼에도 불구하고')으로 명시 재구성, (2) 코드 문자열·주석을 실행 출력까지 현지화하고 문화 레퍼런스는 번역자 이름으로 치환, (3) 원문에 없는 담화 마무리·체감 서술을 보강해 강연 톤을 유지. 이들은 index.md 같은 짧은 표지 파일에서는 거의 관찰되지 않고, 본문량이 큰 article/solution에 집중된다.
