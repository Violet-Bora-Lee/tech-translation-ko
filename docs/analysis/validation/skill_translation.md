
# 마이크로태스크

프라미스 핸들러 `.then`/`.catch`/`.finally`는 항상 비동기적으로 실행됩니다.

프라미스가 즉시 이행(resolve)되더라도 `.then`/`.catch`/`.finally` *아래쪽*에 있는 코드는 이 핸들러들보다 먼저 실행됩니다.

예시를 살펴봅시다.

```js run
let promise = Promise.resolve();

promise.then(() => alert("프라미스 성공!"));

alert("코드 종료"); // 이 얼럿이 가장 먼저 뜹니다.
```

실행해 보면 `코드 종료`가 먼저 보이고 그다음 `프라미스 성공!`이 보입니다.

프라미스는 분명 처음부터 처리가 끝난 상태인데도 이렇게 동작하니 이상하게 느껴집니다.

`.then`은 왜 나중에 실행됐을까요? 그 이유를 알아봅시다.

## 마이크로태스크 대기열

비동기 작업은 적절히 관리되어야 합니다. ECMA 표준은 이를 위해 `PromiseJobs`라는 내부 대기열을 정의하는데, 이 대기열은 흔히 '마이크로태스크 대기열(microtask queue)'이라 불립니다. V8 엔진에서 쓰는 용어죠.

[명세서](https://tc39.github.io/ecma262/#sec-jobs-and-job-queues)에는 다음과 같이 적혀 있습니다.

- 이 대기열은 먼저 들어온 작업을 먼저 실행하는 선입선출(FIFO, first-in-first-out) 구조입니다.
- 다른 작업이 실행 중이 아닐 때만 대기열의 작업이 실행되기 시작합니다.

더 간단히 말하면 프라미스가 준비되었을 때 그 프라미스의 `.then/catch/finally` 핸들러가 대기열에 들어갑니다. 아직 실행되는 것은 아닙니다. 자바스크립트 엔진은 현재 실행 중인 코드가 끝나 여유가 생기면 대기열에서 작업을 꺼내 실행합니다.

앞선 예시에서 `코드 종료`가 먼저 표시된 이유가 바로 이것입니다.

![](promiseQueue.svg)

프라미스 핸들러는 항상 이 내부 대기열을 거칩니다.

여러 개의 `.then/catch/finally`가 체인으로 연결되어 있다면 각 핸들러는 모두 비동기적으로 실행됩니다. 즉, 핸들러는 일단 대기열에 들어간 뒤, 현재 코드가 모두 끝나고 앞서 대기열에 들어간 핸들러들이 실행을 마치면 그때 실행됩니다.

**실행 순서가 중요한 경우엔 어떻게 해야 할까요? `코드 종료`가 `프라미스 성공` 뒤에 나오게 하려면 어떻게 해야 할까요?**

간단합니다. `.then`을 사용해 대기열에 넣기만 하면 됩니다.

```js run
Promise.resolve()
  .then(() => alert("프라미스 성공!"))
  .then(() => alert("코드 종료"));
```

이제 의도한 순서대로 실행됩니다.

## 처리하지 못한 거부

<info:promise-error-handling> 글에서 다룬 `unhandledrejection` 이벤트를 기억하나요?

이제 자바스크립트가 처리하지 못한 거부(unhandled rejection)를 어떻게 감지하는지 정확히 살펴볼 수 있습니다.

**'처리하지 못한 거부'는 마이크로태스크 대기열이 끝나는 시점까지 프라미스 에러가 처리되지 않았을 때 발생합니다.**

보통 에러가 발생할 것으로 예상되면 프라미스 체인에 `.catch`를 추가해 에러를 처리합니다.

```js run
let promise = Promise.reject(new Error("Promise Failed!"));
*!*
promise.catch(err => alert('잡았다'));
*/!*

// 에러가 처리되었으므로 실행되지 않습니다.
window.addEventListener('unhandledrejection', event => alert(event.reason));
```

하지만 `.catch` 추가하는 것을 잊으면 마이크로태스크 대기열이 비워진 뒤 엔진이 이벤트를 발생시킵니다.

```js run
let promise = Promise.reject(new Error("Promise Failed!"));

// Promise Failed!
window.addEventListener('unhandledrejection', event => alert(event.reason));
```

에러를 나중에 처리하면 어떻게 될까요? 아래 예시를 살펴봅시다.

```js run
let promise = Promise.reject(new Error("Promise Failed!"));
*!*
setTimeout(() => promise.catch(err => alert('잡았다')), 1000);
*/!*

// Error: Promise Failed!
window.addEventListener('unhandledrejection', event => alert(event.reason));
```

이제 실행해 보면 `Promise Failed!`가 먼저 보이고 그다음 `잡았다`가 보입니다.

마이크로태스크 대기열을 몰랐다면 "`unhandledrejection` 핸들러가 왜 실행됐지? 에러를 분명히 잡아서 처리했는데!"라고 의아해할 수 있습니다.

하지만 이제 `unhandledrejection`이 마이크로태스크 대기열이 완료되는 시점에 생성된다는 것을 알 수 있습니다. 엔진은 프라미스들을 검사하고, 그중 하나라도 '거부됨(rejected)' 상태이면 이벤트를 발생시킵니다.

위 예시에서 `setTimeout`으로 추가한 `.catch`도 실행됩니다. 다만 이 `.catch`는 `unhandledrejection`이 이미 발생한 뒤에 실행되기 때문에 아무것도 바뀌지 않습니다.

## 요약

모든 프라미스 동작은 내부의 'promise jobs' 대기열을 거치기 때문에 프라미스 핸들링은 항상 비동기적으로 이뤄집니다. 이 대기열은 '마이크로태스크 대기열(microtask queue)'이라고도 불리며, V8 엔진에서 쓰는 용어입니다.

따라서 `.then/catch/finally` 핸들러는 항상 현재 코드가 끝난 뒤에 호출됩니다.

특정 코드가 `.then/catch/finally` 뒤에 실행되도록 보장해야 한다면 그 코드를 체인으로 연결한 `.then` 안에 넣으면 됩니다.

브라우저와 Node.js를 포함한 대부분의 자바스크립트 엔진에서 마이크로태스크 개념은 '이벤트 루프(event loop)', '매크로태스크(macrotask)'와 밀접하게 연관되어 있습니다. 다만 이 둘은 프라미스와 직접적인 관련이 없어서 튜토리얼의 다른 단원인 <info:event-loop> 글에서 다룹니다.
