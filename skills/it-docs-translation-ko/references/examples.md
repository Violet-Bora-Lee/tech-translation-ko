# Examples · 원문↔번역 대조 코퍼스

Annotated before/after pairs illustrating the patterns in `sentence-patterns.md`.

> **Attribution**: All English/Korean excerpts below are quoted from the
> [javascript.info](https://javascript.info) tutorial and its Korean translation
> [ko.javascript.info](https://ko.javascript.info) (© Ilya Kantor and contributors,
> CC BY-NC). Quoted for the purpose of documenting translation techniques.
> These excerpts are not covered by this repository's MIT license.

각 예시의 태그는 sentence-patterns.md의 패턴 번호다.

## 문장 분해 + 담화 연결 [1, 5]

**EN** (1-js/01-getting-started/1-intro/article.md)
> It does not provide low-level access to memory or the CPU, because it was
> initially created for browsers which do not require it.

**KO**
> 메모리나 CPU 같은 저수준 영역의 조작을 허용하지 않습니다. 애초에 이러한 접근이
> 필요치 않은 브라우저를 대상으로 만든 언어이기 때문이죠.

because절을 독립 문장으로 떼고 '~때문이죠'로 인과를 명시했다. 대명사 it은 모두 사라졌다.

## 열거 명시화 [2]

**EN** (1-js/13-modules/03-modules-dynamic-imports/article.md)
> First, we can't dynamically generate any parameters of `import`.

**KO**
> 첫 번째 제약은 `import`문에 동적 매개변수를 사용할 수 없다는 것이었습니다.

'First'가 무엇의 첫 번째인지('제약') 상위 개념을 세워 명시했다. 앞 문단의
'제약사항이 있죠'와 결속되고, 회고 맥락이라 과거형으로 호응한다.

## 정보 블록 재배치 [3]

**EN** (2-ui/2-events/02-bubbling-and-capturing/article.md)
> 1. `HTML` → `BODY` → `FORM` → `DIV` → `P` (capturing phase, the first listener):
> 2. `P` → `DIV` → `FORM` → `BODY` → `HTML` (bubbling phase, the second listener).
>
> Please note, the `P` shows up twice, because we've set two listeners…

**KO**
> 1. `HTML` → `BODY` → `FORM` → `DIV` (캡처링 단계, 첫 번째 리스너)
> 2. `P` (타깃 단계, 캡쳐링과 버블링 둘 다에 리스너를 설정했기 때문에 두 번 호출됩니다.)
> 3. `DIV` → `FORM` → `BODY` → `HTML` (버블링 단계, 두 번째 리스너)

2단계 리스트에 숨어 있던 타깃 단계를 독립 항목으로 끌어올려 개념 구조(캡처링→타깃→버블링)를
리스트 모양 자체로 드러냈다. 별도 문장이던 중복 설명은 항목 안 괄호로 흡수했다.

## 지시 대상 복원 [4]

**EN** (1-js/11-async/05-promise-error-handling 계열)
> But if any of the promises above rejects…, then it would catch it.

**KO**
> 그런데 네트워크 문제, 잘못된 형식의 JSON 등으로 인해 프라미스 중 하나라도 거부되면
> `.catch`에서 거부된 프라미스를 처리합니다.

it…it을 '`.catch`'와 '거부된 프라미스'로 각각 복원했다.

## 독자 보강 [6]

**EN** (1-js/01-getting-started/4-devtools/article.md)
> The developer tools will open on the Console tab by default.

**KO**
> 개발자 도구가 보일 겁니다. 개발자 도구를 처음 열어보셨다면 Console 패널이
> 기본으로 보입니다.

원문에 없는 '처음 열어보셨다면' 조건을 신설해 초심자를 배려했다.

**EN** (1-js/03-code-quality/06-polyfills/article.md)
> (it's big, we have a lot to study yet)

**KO**
> 표가 상당히 큰데, 각 기능에 대해선 차근차근 배울 예정이니 너무 겁먹지 않으셔도 됩니다.

괄호 여담을 독자를 안심시키는 완결 문장으로 확장했다.

## 리듬 변주 [7]

**EN** (7-animation/1-bezier-curve/article.md)
> For instance, two points curve: / Three points curve: / Four points curve:

**KO**
> 조절점이 두 개인 베지어 곡선을 살펴봅시다. / 조절점이 세 개인 베지어 곡선은 다음과
> 같습니다. / 네 개의 조절점이 있을 땐 다음과 같은 곡선이 나옵니다.

동일 구조 3연속을 문형 셋으로 변주하고 명사구+쌍점 라벨을 완결 문장으로 바꿨다.

## 헤딩 재작성 [8]

**EN** (2-ui/1-document/05-basic-dom-node-properties/article.md)
> ## innerHTML: the contents / ## outerHTML: full HTML of the element

**KO**
> ## innerHTML로 내용 조작하기 / ## outerHTML로 요소의 전체 HTML 보기

'용어: 설명' 쌍점 헤딩을 동작 중심으로 재작성해 쌍점도 함께 사라졌다.

## 예시 현지화 [9]

**EN** (1-js/06-advanced-functions/02-rest-parameters-spread/article.md)
> `showName("Julius", "Caesar", "Consul", "Imperator");`
> `// i.e. titles = ["Consul", "Imperator"]`

**KO**
> `showName("Bora", "Lee", "Software Engineer", "Researcher");`
> `// titles = ["Software Engineer", "Researcher"]`

인명·직함을 현지화하되 코드 주석과 예상 출력까지 함께 바꿔 예시 전체의 정합성을 유지했다.

**EN** (2-ui/1-document/05-basic-dom-node-properties/article.md)
> `let name = prompt("What's your name?", "<b>Winnie-the-Pooh!</b>");`

**KO**
> `let name = prompt("이름을 알려주세요.", "<b>이보라</b>");`

## 코드 주석의 의도 번역 [formatting]

**EN** (1-js/11-async/07-microtask-queue/article.md)
> `alert("code finished"); // this alert shows first`

**KO**
> `alert("코드 종료"); // 얼럿 창이 가장 먼저 뜹니다.`

주석을 직역하지 않고 실행 결과를 서술하는 완결 문장으로 옮겼다. UI 문자열도 번역했다.

## 재량의 한계 사례 [10]

**EN** (1-js/11-async/07-microtask-queue/article.md)
> But it does so later, after unhandledrejection has already occurred,
> so it doesn't change anything.

**KO**
> 다만 `.catch`는 `unhandledrejection`이 발생한 이후에 트리거 되므로
> `프라미스 실패!`가 출력됩니다.

추상 결론("아무것도 바꾸지 않는다")을 관찰 가능한 출력으로 치환한 보강이지만, 원문
뉘앙스에서 다소 이탈했다. 보강이 의미를 좁히기 시작하면 재량의 한계선이다.
