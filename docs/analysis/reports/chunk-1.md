# chunk-1 분석 보고서

- 분석 파일 수: 30개 (chunks.json 인덱스 1)
- 대조 방식: ko/en 문단 단위 대조. 긴 article 3개(debugging-chrome, polyfills, rest-parameters-spread)를 집중 분석하고 나머지 index·solution·task 27개에서 패턴 빈도를 확인했다.
- 주의: `06-polyfills/article.md`는 ko(55줄)와 en(90줄)의 섹션 구성·줄 수가 어긋나는 **버전 불일치** 파일이다. 두 파일은 첫 인트로 문단만 정렬되고 이후 완전히 다르다(ko는 구버전 원본을 번역). 따라서 이 파일의 '설명 추가'는 번역자의 보강(H)이 아니라 서로 다른 원본이므로 H 관찰 대상에서 제외했다. 정렬이 유효한 인트로 문단만 부분 인용했다.

## 카테고리별 관찰 빈도

| 카테고리 | 관찰 빈도(파일 수) | 성격 |
|---|---|---|
| A. 문장 분해·재구성 | 다수 (article 3개 전반, 짧은 파일 다수) | 암묵지 |
| B. 어순·정보구조 재배치 | 다수 (제목 구체화 포함) | 암묵지 |
| C. 인칭·대명사 처리 | 거의 전 파일 | wiki 명문 |
| D. 어휘 선택·용어 | 다수 (한-영 병기, 인명 현지화, 유의어 교체) | 일부 암묵지 |
| E. 어미·문체 | 거의 전 파일 | wiki 명문 |
| F. 문장부호·표기 | 다수 | wiki 명문 |
| G. 코드 요소 처리 | article 3개 + solution 일부 | 암묵지 |
| H. 생략·보강 | article 2개(debugging, rest) | 암묵지 |
| I. 담화 연결 | debugging 집중, 산발 | 암묵지 |
| J. 신규 패턴 | 아래 J 항목 참조 | 암묵지 |

---

## 주목할 암묵지 패턴 (상세)

### [D] 인명·고유명사·예시 데이터 현지화
- 원문: `showName("Julius", "Caesar", "Consul", "Imperator");` / `// i.e. titles = ["Consul", "Imperator"]` / `showName("Ilya");`
- 번역: `showName("Bora", "Lee", "Software Engineer", "Researcher");` / `// titles = ["Software Engineer", "Researcher"]` / `showName("Bora");`
- 위치: 06-advanced-functions/02-rest-parameters-spread/article.md:51-62, 92-96
- 설명: 로마 인명(Julius Caesar, Consul, Imperator)을 한국 독자에게 친숙한 이름·직함(Bora Lee, Software Engineer)으로 교체했다. 본문뿐 아니라 **코드 주석과 alert 예상 출력 주석까지** 일관되게 바꿔 예시 전체의 정합성을 유지한 점이 핵심이다. 코드 로직은 그대로 두고 데이터만 현지화한다.
- 반복 사례: 06-advanced-functions/03-closure/1-closure-latest-changes/solution.md:1 — 정답 인물 `Pete`→`지민`. 원문 인명이 답 텍스트에 직접 등장하는 경우까지 현지화 대상에 포함한다. (총 2개 파일, 인스턴스 5+회)

### [A/I] 압축 문장을 인과·리듬으로 풀어 재구성
- 원문: `Such command works only when the development tools are open, otherwise the browser ignores it.`
- 번역: `debugger 명령어를 사용하면 브라우저를 켜 개발자 도구를 열고 소스 코드 영역을 띄워 중단점을 설정하는 수고를 하지 않아도 됩니다. 에디터를 떠나지 않고도 중단점을 설정할 수 있기 때문에 편리하죠.`
- 위치: 03-code-quality/01-debugging-chrome/article.md:87
- 설명: 한 문장을 두 문장으로 분해하면서 원문에 없던 '왜 편리한가'(에디터를 떠나지 않아도 됨)를 보강하고 `~때문에`로 인과를 명시, `~죠`로 리듬을 더했다. 원문의 정보 전달을 넘어 독자 설득까지 수행하는 재구성이다.
- 반복 사례: 같은 파일 다수. `1+2` results in `3`... → `1+2를 입력하면 3이 출력되고... undefined가 출력되는 이유는 ~ 때문입니다`(41행), `no function there, so it's called "anonymous"` → 별도 문장으로 분리 후 인과 접속(106행). (debugging 파일에서 10회 이상)

### [B/D] 제목의 구체화·의미 명시
- 원문: `# Debugging in the browser` / `# Which day of month was many days ago?` / `# Polyfills and transpilers`
- 번역: `# Chrome으로 디버깅하기` / `# n일 전 '일' 출력하기` / `# 폴리필`
- 위치: 03-code-quality/01-debugging-chrome/article.md:1, 05-data-types/11-date/4-get-date-ago/task.md:6, 03-code-quality/06-polyfills/article.md:2
- 설명: 일반명사 제목(in the browser)을 본문에서 실제 다루는 대상(Chrome)으로 좁히거나, 의문형 제목을 과제 동작을 서술하는 평서형(`n일 전 '일' 출력하기`)으로 바꾼다. 헤딩 물음표는 제거된다(F 규칙과 결합). 강조는 작은따옴표(`'일'`)로 표기.

### [G] 코드 주석·smart header 번역, 예시 출력은 원문 유지
- 원문: `debugger;  // <-- the debugger stops here` / ` ```smart header="Conditional breakpoints" ` / `console.log("value,", i);`
- 번역: `debugger;  // <-- 여기서 실행이 멈춥니다.` / ` ```smart header="조건부 중단점" ` / `console.log("숫자", i);`
- 위치: 03-code-quality/01-debugging-chrome/article.md:80, 65, 176
- 설명: 코드 내 **한글 설명 주석과 smart 블록 header는 번역**하되, 코드 식별자·API명(`debugger`, `console.log`)은 원문 유지한다. `console.log`의 출력 문자열 리터럴(`"value,"`→`"숫자"`)까지 번역해 콘솔 출력 예시를 한글화한 점이 세밀하다. 단 alert 예상 결과 주석의 값(`// 5`, `// H,e,l,l,o`)은 코드 실행 결과이므로 그대로 둔다.

### [D] 한-영 병기와 음차 정착
- 원문: `Breakpoints` / `Call Stack` / `transpiler`
- 번역: `중단점(breakpoint)` / `콜 스택(Call Stack)` / `트랜스파일러(transpiler)`
- 위치: debugging-chrome 전반, rest-parameters-spread 전반
- 설명: 핵심 용어 첫 등장 시 `한글(영문)` 병기 후 이후엔 한글만 쓰거나, UI에 실제 뜨는 문자열(`Call Stack`, `Watch`, `Resume`)은 영문을 유지한다. `전개 구문(spread syntax, 스프레드 구문)`처럼 번역어·음차를 함께 제시해 두 표기를 모두 노출하는 사례도 있다(02-rest-parameters:151).

### [H] 독자 배려 보강 (정렬 유효 구간 한정)
- 원문: `(it's big, we have a lot to study yet)`
- 번역: `표가 상당히 큰데, 각 기능에 대해선 차근차근 배울 예정이니 너무 겁먹지 않으셔도 됩니다.`
- 위치: 03-code-quality/06-polyfills/article.md:10 (인트로 정렬 구간)
- 설명: 괄호 속 짧은 여담을 독자를 안심시키는 완결된 문장('너무 겁먹지 않으셔도')으로 확장했다. 정보량 대비 정서적 배려를 더하는 보강이다.
- 반복 사례: debugging-chrome:194 `please go there and look through...` → `~들어가 더 많은 개발자 도구 기능에 대해 알아보시기 바랍니다`처럼 권유를 풀어쓰는 보강 산발.

---

## wiki 명문 규칙 확인 (빈도만)

- **C. 인칭대명사 생략** (we/you/it → 생략): 거의 전 파일. `We'll be using Chrome` → `Chrome 브라우저에서 제공하는 디버깅 툴을 사용하도록 하겠습니다`(주어 생략), `You've set a breakpoint` → `중단점을 성공적으로 설정하셨습니다`. (30개 중 서술형 텍스트 있는 전 파일)
- **E. 어미·문체**:
  - 합니다체 통일: 전 파일.
  - 청유형 `~해봅시다/~살펴봅시다`: debugging, rest, task 다수. `Let's talk about debugging` → `디버깅이란 것에 대해 이야기해봅시다`. (15+ 파일)
  - 리듬 어미 `~죠/~이시죠?`: debugging 집중. `blue is where you should click` → `파란색으로 바뀐 게 보이시죠?`. (5+ 회)
- **F. 문장부호·표기**:
  - 헤딩 물음표 제거: `Last day of month?` → `달의 마지막 일`, `Which day...ago?` → `n일 전 '일' 출력하기`. (3 파일)
  - 강조 작은따옴표: `'여분의'`, `'있는 그대로'`, `'확장'`. 큰따옴표는 직접 인용·UI 문자열에만. (다수)
  - 명사 종결 무마침표: index.md 제목들.
- **D. `P.S.` 처리**: `P.S.` → `주의:`(sum-input, get-date-ago) 또는 `참고:`(counter-inc-dec). 라벨 뒤 쌍점은 리스트 라벨 예외로 허용. (3 파일)

## J. 신규 패턴

### [J] 열거 항목의 명시적 조건 재서술
- 원문: `Otherwise, if less than an hour, then "m min. ago".`
- 번역: `그렇지 않고, date가 지금으로부터 1시간 미만 전의 날짜를 나타내면 "n분 전"을 반환해야 합니다.`
- 위치: 05-data-types/11-date/8-format-date-relative/task.md:9-12
- 설명: 영어의 생략형 열거(`Otherwise, if less than an hour`)에서 생략된 주어·목적어(`date가`, `~날짜를 나타내면`, `~반환해야 합니다`)를 매 항목마다 반복 복원해 각 조건을 독립적으로 읽을 수 있게 했다. 앞 항목을 참조해야 이해되는 압축을 풀어 항목 단위 자기완결성을 확보하는 기법. 또한 플레이스홀더 `m min.`을 한글 관례 `n분`으로 통일(변수 기호도 현지 관례화).
