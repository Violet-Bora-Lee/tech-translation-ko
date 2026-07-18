# 청크 2 대조 분석 보고서

## 개요

- 분석 파일 수: 11개 (article 3, index 5, solution 2, task 1)
- 대상: `1-js/11-async` ~ `2-ui/1-document` 영역
- 큰 article 3개(microtask-queue, dynamic-imports, basic-dom-node-properties)에 암묵지 패턴이 집중됨. index 5개는 한 문장짜리 헤딩·리드로 관찰량이 적음.

## 카테고리별 관찰 빈도

| 카테고리 | 빈도 | 비고 |
|---|---|---|
| A. 문장 분해·재구성 | 12 | 평서문→청유형/의문형 전환, 짧은 문장 병합 |
| B. 어순·정보구조 재배치 | 8 | 열거 구조 명시화("First,"→"첫 번째 제약은~") |
| C. 인칭·대명사 처리 | 15+ | we/you/it 생략 상시. wiki 명문 규칙 |
| D. 어휘 선택·용어 | 14 | 한-영 병기, tree-shaken→가지치기, 문화적 현지화 |
| E. 어미·문체 | 20+ | 합니다체, '-죠/-네요' 리듬 어미, 청유형 상시 |
| F. 문장부호·표기 | 10 | 큰따옴표→작은따옴표, 쌍점. wiki 명문 규칙 |
| G. 코드 요소 처리 | 16 | 주석·alert 문자열 번역, 주석 보강, smart header |
| H. 생략·보강 | 11 | 원문 부정확성 교정, 배경 정보 보강 |
| I. 담화 연결 | 9 | 대조·인과 접속어 삽입 |
| J. 신규 패턴 | 4 | 문화적 현지화, 원문 교정, 제목 재정의 |

---

## H. 생략·보강 (암묵지 핵심)

### [H] 원문의 불완전한 코드 표기를 정확한 형태로 교정하며 번역
- 원문: `Here we have a more complex call (expression)().` / `The similar thing as (3), to the left of the parentheses () we have an expression.`
- 번역: `좀 더 복잡한 패턴의 호출(`(expression).method()`)이 등장했네요.` / ``(3)`과 동일한 패턴의 호출입니다. `expression`이 `obj.go || obj.stop`라는 차이점만 있습니다.`
- 위치: 1-js/99-js-misc/04-reference-type/3-why-this/solution.md:8, 17
- 설명: 원문은 4번을 "괄호 왼쪽에 표현식이 있다"고만 뭉뚱그렸는데, 번역자는 실제 예제 코드를 확인해 `expression`의 구체값 `obj.go || obj.stop`을 명시하고 3번 호출 형태도 `(expression).method()`로 정확히 다시 적었다. 독자가 예제와 설명을 왕복하지 않아도 되게 만든 보강이다.

### [H] 참조 타입의 내부 구조를 원문에 없이 괄호로 덧붙임
- 원문: `property accessors (dot or square brackets) return a value of the Reference Type.`
- 번역: `점이나 대괄호를 통해 프로퍼티에 접근하려는 경우 참조 타입 값(`(base, name, strict)`)이 반환됩니다.`
- 위치: 1-js/99-js-misc/04-reference-type/3-why-this/solution.md:19
- 설명: 참조 타입이 실제로 담는 3요소 `(base, name, strict)`를 원문에 없이 삽입했다. 본문(article)에서 다룬 개념을 solution에서 상기시키는 크로스 보강.

### [H] 원문의 짧은 삽입구를 독립 문장으로 확장해 정서·맥락 부여
- 원문: `reloads smile.gif (hope it's cached).`
- 번역: ``smile.gif` 역시 다시 로딩되는 것이죠. 어딘가에 이런 리소스들을 캐싱해 놓았다면 좋았을 거라는 생각이 드는 순간이네요.`
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:267
- 설명: 괄호 삽입구 "(hope it's cached)"를 독립 문장으로 풀어 화자의 아쉬움을 드러냈다. Viki 문체의 '독자에게 말 걸기'와 통하는 정서적 확장.

### [H] 결론 문장을 원문에 없이 덧붙여 논지를 매듭지음
- 원문: (해당 문장 없음)
- 번역: `이로써 앞선 의문이 자연스레 해결되었습니다.`
- 위치: 1-js/11-async/07-microtask-queue/article.md:100
- 설명: 앞서 던진 "왜 unhandledrejection이 실행되지?"라는 의문에 대한 회수 문장을 추가했다. 원문은 설명만 하고 끝나는데, 번역은 질문-답 구조를 명시적으로 닫아 담화 완결성을 높였다.

### [H] 원문의 추상적 결론을 구체적 관찰 결과로 치환
- 원문: `But it does so later, after unhandledrejection has already occurred, so it doesn't change anything.`
- 번역: `다만 `.catch`는 `unhandledrejection`이 발생한 이후에 트리거 되므로 `프라미스 실패!`가 출력됩니다.`
- 위치: 1-js/11-async/07-microtask-queue/article.md:102
- 설명: "아무것도 바꾸지 않는다"는 추상 결론을, 실제 콘솔에 뜨는 문자열 "프라미스 실패!"로 바꿔 관찰 가능한 사실로 만들었다. (다만 원문 뉘앙스에서 다소 이탈한 재해석)

### [H] 원문 압축 항목을 완전한 문장 리스트로 풀어 씀
- 원문: `Text nodes are not the same as element nodes.`
- 번역: `텍스트 노드는 요소 노드와 다른 프로퍼티를 지원하는 것은 말할 필요도 없습니다.`
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:9
- 설명: 단순 대비문을 "말할 필요도 없습니다"라는 강조 어투로 확장해 텍스트 노드가 다른 프로퍼티를 갖는다는 함의까지 명시했다.

---

## J. 신규 패턴

### [J] 문화적 현지화: 예시 인물명을 번역자 본인 이름으로 교체
- 원문: `let name = prompt("What's your name?", "<b>Winnie-the-Pooh!</b>");` / `we see the bold name`
- 번역: `let name = prompt("이름을 알려주세요.", "<b>이보라</b>");`
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:400
- 설명: 영미권 캐릭터 "Winnie-the-Pooh"를 한국 독자에게 친숙하도록 번역자 실명 "이보라"로 바꿨다. 코드 문자열 리터럴 내부까지 현지화한 사례로, 개념 전달에 무관한 고유명사는 자유롭게 치환한다는 판단이 드러난다.

### [J] 챕터 index 제목을 원문 직역이 아닌 실제 수록 내용으로 재정의
- 원문: `# Generators, advanced iteration`
- 번역: `# 제너레이터와 비동기 이터레이션`
- 위치: 1-js/12-generators-iterators/index.md:2
- 설명: "advanced iteration"을 직역("고급 이터레이션")하지 않고 챕터가 실제로 다루는 "비동기 이터레이션"으로 특정했다. 제목을 독자가 검색할 실제 주제어로 맞춘 편집적 판단.

### [J] 헤딩을 기능 설명형으로 재작성
- 원문: `## Tag: nodeName and tagName` / `## nodeValue/data: text node content`
- 번역: `## nodeName과 tagName으로 태그 이름 확인하기` / `## nodeValue/data로 텍스트 노드 내용 조작하기`
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:171, 349
- 설명: "명사: 명사" 형식의 원문 헤딩을 "~로 ~하기" 동작 설명형으로 재구성했다. 쌍점을 제거하는 동시에 헤딩만 봐도 무엇을 하는 절인지 알 수 있게 만들었다. 다수 헤딩에 일관 적용.

### [J] 원문에 있던 클래스 항목을 통째로 생략·재편
- 원문: Document, CharacterData(Text/Comment 하위), Finally HTMLElement 등 개별 클래스 항목이 각각 존재
- 번역: Document·CharacterData 항목을 생략하고 Node 항목 안에 Text/Element/Comment를 압축 서술
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:22
- 설명: 원문의 상세 클래스 나열을 축약해 핵심 상속 계층만 남겼다. 정보 밀도가 높은 원문을 학습 흐름에 맞춰 재편한 구조 편집(주의: 정보 손실을 감수한 의역).

---

## I. 담화 연결

### [I] 대조 접속어를 문단 도입부에 삽입
- 원문: `But how can we import a module dynamically, on-demand?`
- 번역: `그럼에도 불구하고 모듈을 동적으로 불러와야 한다면 어떻게 해야 할까요?`
- 위치: 1-js/13-modules/03-modules-dynamic-imports/article.md:27
- 설명: "But"을 "그럼에도 불구하고"로 명시해 앞 문단(정적 import의 제약이 필요한 이유)과의 대조를 강화했다. (관찰 9회, 대표 1건)

### [I] 병렬 문장 사이에 인과를 명시
- 원문: `Normally, if we expect an error, we add .catch to the promise chain to handle it:`
- 번역: `정상적인 경우라면 개발자는 에러가 생길 것을 대비하여 프라미스 체인에 `.catch`를 추가해 에러를 처리합니다.`
- 위치: 1-js/11-async/07-microtask-queue/article.md:63
- 설명: "we"를 생략하지 않고 "개발자는"이라는 구체 행위자로 치환하며 "대비하여~처리합니다"로 목적-수단 관계를 이었다.

---

## G. 코드 요소 처리

### [G] 코드 주석을 번역하며 결과 설명을 보강
- 원문: `alert("code finished"); // this alert shows first`
- 번역: `alert("코드 종료"); // 얼럿 창이 가장 먼저 뜹니다.`
- 위치: 1-js/11-async/07-microtask-queue/article.md:15
- 설명: 주석을 직역("이 얼럿이 먼저 표시됨")이 아니라 "얼럿 창이 가장 먼저 뜹니다"라는 완결된 서술로 번역. 주석도 자연어로 취급하는 원칙. (주석 번역 관찰 다수)

### [G] alert·prompt 내 UI 문자열 전면 한글화
- 원문: `alert("promise done!")` / `alert('caught')` / `prompt("Which module to load?")`
- 번역: `alert("프라미스 성공!")` / `alert('잡았다!')` / `prompt("어떤 모듈을 불러오고 싶으세요?")`
- 위치: 1-js/11-async/07-microtask-queue/article.md:13, 68 등
- 설명: 사용자에게 보이는 출력 문자열은 모두 한글로 옮긴다. 반면 코드 식별자(변수명·함수명)와 에러 클래스는 원문 유지. 관찰 16회 이상.

### [G] smart header 속성값까지 번역
- 원문: ` ```smart header="console.dir(elem) versus console.log(elem)" `
- 번역: ` ```smart header="`console.dir(elem)`과 `console.log(elem)`의 차이" `
- 위치: 2-ui/1-document/05-basic-dom-node-properties/article.md:69, 80
- 설명: smart 블록의 header 속성 문자열도 번역 대상. "versus"를 "의 차이"로 자연스럽게 옮겼다.

---

## A. 문장 분해·재구성

### [A] 평서 감탄문을 청유형으로 전환해 학습 유도
- 원문: `Why did the .then trigger afterwards? What's going on?`
- 번역: `왜 `.then`이 나중에 트리거 되었을까요? 그 이유에 대해 알아봅시다.`
- 위치: 1-js/11-async/07-microtask-queue/article.md:22
- 설명: 두 번째 의문문 "What's going on?"을 청유형 "알아봅시다"로 바꿔 다음 절로 자연스럽게 넘어가게 했다. 원문의 수사적 질문을 학습 안내로 재기능화. (관찰 12회)

### [A] 두 문장을 인과로 묶어 한 문장으로 병합
- 원문: `That's strange, because the promise is definitely done from the beginning.`
- 번역: `프라미스는 즉시 이행상태가 되었는데도 말이죠. 뭔가 이상하네요.`
- 위치: 1-js/11-async/07-microtask-queue/article.md:20
- 설명: 반대로 원문 한 문장을 두 개로 쪼개고 순서를 뒤집었다(결과→'-네요' 감탄을 뒤로). 짧은 문장 여러 개로 리듬을 만드는 Viki 문체와 일치.

---

## B. 어순·정보구조 재배치

### [B] 열거 순서어를 명시적 주어구로 승격
- 원문: `First, we can't dynamically generate any parameters of import.` / `Second, we can't import conditionally or at run-time:`
- 번역: `첫 번째 제약은 `import`문에 동적 매개변수를 사용할 수 없다는 것이었습니다.` / `두 번째 제약은 런타임이나 조건부로 모듈을 불러올 수 없다는 점이었습니다.`
- 위치: 1-js/13-modules/03-modules-dynamic-imports/article.md:5, 13
- 설명: 부사 "First/Second"를 "첫 번째 제약은~"이라는 주어구로 올려 무엇을 열거하는지 명시했다. 앞 문단의 "제약사항이 있죠"를 받아 과거형("~것이었습니다")으로 호응시킨 점도 담화 연결. 코드북 B의 대표 기법.

---

## E. 어미·문체 (빈도 중심)

### [E] '-죠/-네요/-군요' 리듬 어미와 청유형 상시 사용
- 대표: `프라미스는 즉시 이행상태가 되었는데도 말이죠.` (microtask:20), `물론 있습니다. 미묘하지만 이름에서 그 차이를 유추할 수 있죠.` (basic-dom:161)
- 설명: 단조로운 '-습니다' 종결을 피해 문단마다 '-죠', '-네요', 청유형('살펴봅시다', '~해봅시다')을 섞는다. wiki 명문 규칙과 Viki 문체 양쪽에 부합. 20회 이상.

---

## C·F 명문 규칙 확인 (빈도만)

- **C. 인칭·대명사 생략/명시**: we/you/it 생략 15회 이상. "we"를 "개발자는"으로 구체화한 사례(microtask:63)는 Viki 문체의 명시성 우선과 일치.
- **F. 큰따옴표→작은따옴표**: 강조어 "events"→'이벤트', "code finished"→'코드 종료' 등 8회. 큰따옴표는 코드·직접 인용에만 유지.
- **F. 쌍점 제거**: 헤딩 "Tag: nodeName"→"nodeName과 tagName으로~" 등에서 쌍점 제거. 리스트 라벨의 쌍점은 유지.
</content>
</invoke>
