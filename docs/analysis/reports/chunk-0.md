# Chunk 0 대조 분석 보고서

- 분석 파일 수: 16개 (index 6, article 4, solution 4, task 2)
- 대상: `1-js/` 도입부(getting-started, first-steps, code-quality)
- 분석 대상 중 본문 분량이 큰 `1-intro/article.md`, `4-devtools/article.md`, `04-ninja-code/article.md`, `2-manuals-specifications/article.md`에서 암묵지 패턴 대부분이 관찰됨. solution/task/index는 짧아 명문 규칙 확인 위주.

## 카테고리별 관찰 빈도

| ID | 카테고리 | 빈도 | 성격 |
|----|----------|------|------|
| A | 문장 분해·재구성 | 다수(20+) | 암묵지 |
| B | 어순·정보구조 재배치 | 8 | 암묵지 |
| C | 인칭·대명사 처리 | 다수(전 파일) | 명문 규칙 |
| D | 어휘 선택·용어 | 15+ | 혼합 |
| E | 어미·문체 | 다수(전 파일) | 명문 규칙 |
| F | 문장부호·표기 | 10+ | 명문 규칙 |
| G | 코드 요소 처리 | 9 | 암묵지 |
| H | 생략·보강 | 18+ | 암묵지(최우선) |
| I | 담화 연결 | 12 | 암묵지 |
| J | 신규 패턴 | 3 | 암묵지 |

---

## H. 생략·보강 (가장 밀도 높은 암묵지)

### [H] 원문의 추상 서술을 실제 화면·구체 사실로 치환
- 원문: In this case, the script contains an unknown "lalala" command. / On the right, there is a clickable link to the source `bug.html:12` with the line number
- 번역: 'lalala'가 정의되지 않았다(not defined)라는 메시지입니다. / 에러 메시지 우측에 링크 `bug.html:12`가 있습니다. bug.html은 해당 에러가 발생한 파일, 12는 에러가 발생한 줄을 나타냅니다.
- 위치: 4-devtools/article.md:29-30
- 설명: 원문의 'unknown command'를 실제 콘솔에 뜨는 문구 'not defined'로 바꾸고, `bug.html:12`의 파일명·줄번호 의미를 쪼개 설명한다. 독자가 화면에서 보게 될 것과 번역문을 일치시키는 보강. Viki 패턴 22(실제 화면과 어긋난 서술 교정)와 동일 방향.

### [H] 결론 문장 앞에 독자 상황을 가정하는 문장을 신설
- 원문: The developer tools will open on the Console tab by default.
- 번역: 개발자 도구가 보일 겁니다. 개발자 도구를 처음 열어보셨다면 Console 패널이 기본으로 보입니다.
- 위치: 4-devtools/article.md:21
- 설명: 한 문장을 '도구가 열린다 + 처음이라면 Console이 기본'으로 나누며 원문에 없는 '처음 열어보셨다면' 조건을 보강해 초심자를 배려한다.

### [H] 개념어에 부연 설명·범주 명사를 덧붙임
- 원문: contains the most in-depth, detailed and formalized information about JavaScript
- 번역: 자바스크립트와 관련된 가장 심도 있고 상세한 정보를 담고 있는 공식 문서입니다
- 위치: 2-manuals-specifications/article.md:8
- 설명: 원문에 없는 '공식 문서'라는 범주 명사를 보강해 ECMA-262의 위상을 명시한다. 이어지는 문장에서도 'ECMA-262 명세서'로 주어를 반복 명시(패턴 C의 반대 방향 보강)해 지시 대상을 분명히 한다.

### [H] 캐릭터·프레임을 강화하는 보강 (ninja 문서 전반)
- 원문: Let an unfamiliar reader think well over similarly named function `printMessage`
- 번역: 유지보수를 담당한 지 얼마 안 된 개발자가 코드를 곱씹을 수 있도록 여러 곳에 훈련 장치를 배치해 놓아야 합니다.
- 위치: 03-code-quality/04-ninja-code/article.md:129 (원문 en:123)
- 설명: 원문에 없는 '유지보수를 담당한 지 얼마 안 된 개발자', '훈련 장치를 배치'를 보강해 닌자 프레임을 한국어 독자에게 더 선명하게 전달한다. 문서 전반에서 '훈련/극기 훈련' 은유를 반복 삽입하고(:53, :165), 원문에 없는 문장('회사에서 당신의 입지는 더 넓어지겠죠' :216)을 추가하기도 한다. 관찰 6회.

### [H] 자명한 추론 문장을 통째로 압축하는 편집적 생략
- 원문: No difference! In both cases, `return confirm('Did parents allow you?')` executes exactly when the `if` condition is falsy.
- 번역: 동일하게 동작합니다.
- 위치: 02-first-steps/15-function-basics/1-if-else-required/solution.md:1
- 설명: 결론 + 근거 두 문장을 한 어절 결론으로 압축해 버렸다. 코드가 바로 위에 노출된 짧은 solution에서는 근거 설명이 군더더기라 판단해 과감히 삭제한 편집적 생략. 이 청크에서 가장 극적인 생략 사례.

### [H] 원문 군더더기·중복 표현 생략
- 원문: Novice developers sometimes use them even better than programmer ninjas.
- 번역: 어떨 때는 초보 개발자가 닌자보다 더 적극적으로 나서서 이런 편법을 사용하곤 합니다.
- 위치: 04-ninja-code/article.md:13
- 설명: 'programmer ninjas'의 반복을 '닌자'로 압축. 반대로 'them'은 '이런 편법'으로 풀어(패턴 C) 정보 손실 없이 다듬는다.

---

## J. 신규 패턴 (주목)

### [J] 인용구·격언의 현지화 대체 (author까지 교체)
- 원문: ```quote author="Laozi (Tao Te Ching)" / The Tao that can be told is not the eternal Tao. The name that can be named is not the eternal name.
- 번역: ```quote author="공자" / 모든 일 중 가장 어려운 일은<br>어두운 방에서 검은 고양이를 찾는 일이다.<br><br>특히 그 방에 고양이가 없을 때에.
- 위치: 04-ninja-code/article.md:107-113
- 설명: 원문 인용구(도덕경)를 전혀 다른 격언('어두운 방 검은 고양이')으로 대체하고 저자 속성도 공자로 바꿨다. 원문 quote를 직역하지 않고 문맥(디버깅의 어려움)에 맞는 다른 명언으로 갈아끼우는 대담한 현지화. 다른 quote들은 한국 고전 번역체로 시적 재작성(:4 공자, :42 노자).

### [J] 반어·유머 헤더의 톤 재창작
- 원문: ```warn header="Irony detected" / Many try to follow ninja paths. Few succeed.
- 번역: ```warn header="방금 들어온 속보입니다!" / 닌자 같은 무림 고수가 되는 게 꿈인 개발자는 많지만, 그 목표를 달성하는 건 아주 극소수라는 소식입니다.
- 위치: 04-ninja-code/article.md:18-20
- 설명: 'Irony detected'를 '방금 들어온 속보입니다!'로 바꾸고 본문도 뉴스 앵커 어투('~라는 소식입니다')로 재창작해 반어 톤을 한국어 관습으로 옮겼다. 'ninja'에 '무림 고수' 비유를 얹어 문화적 등가물을 보강.

### [J] 이미지 확장자 등 로컬 자산 맞춤 교체
- 원문: ![chrome](chrome.webp)
- 번역: ![chrome](chrome.png)
- 위치: 4-devtools/article.md:25
- 설명: 이미지 확장자를 webp→png로 교체해 로컬 저장소 자산에 맞췄다. 번역자의 의도적 현지화 선택으로 볼 수 있는 실제 편집.

> 주의(기법 아님 — 버전 드리프트): 엔진 코드네임 목록(:29, 원문 en은 V8에 Edge 포함·Chakra/JavaScriptCore/Nitro 나열, ko는 Trident/ChakraCore/SquirrelFish로 재편)과 intro의 transpile 언어 목록에서 Brython·Kotlin 누락(:112~114)은 번역 기법이 아니라 ko가 더 오래된 en 판본을 따라간 원본 버전 차이일 공산이 크다. 패턴 추출 대상에서 제외한다.

---

## A. 문장 분해·재구성 (빈번, 대표례)

### [A] 등위접속 장문을 두 문장으로 분해
- 원문: Today, JavaScript can execute not only in the browser, but also on the server, or actually on any device that has a special program called the JavaScript engine.
- 번역: 자바스크립트는 브라우저뿐만 아니라 서버에서도 실행할 수 있습니다. 이 외에도 [자바스크립트 엔진]이라 불리는 특별한 프로그램이 들어 있는 모든 디바이스에서도 동작합니다.
- 위치: 1-intro/article.md:21
- 설명: 'not only A but also B, or C' 구조를 'A/B는 한 문장, C는 별도 문장'으로 끊고 '이 외에도'로 연결(패턴 I 결합). 관찰 20회 이상.

### [A] 평서문 결과 서술을 청유·유도문으로 전환
- 원문: For instance, take a look at this ternary operator `'?'`:
- 번역: 조건부 연산자 `'?'`를 사용한 예시를 살펴봅시다.
- 위치: 04-ninja-code/article.md:29
- 설명: 명령문을 '~살펴봅시다' 청유형으로 바꿔 독자에게 말을 건다(패턴 E). 쌍점도 제거(패턴 F).

---

## B. 어순·정보구조 재배치

### [B] 수식 정보를 표제어 앞으로 이동
- 원문: **MDN (Mozilla) JavaScript Reference** is the main manual with examples and other information.
- 번역: Mozilla 재단이 운영하는 **MDN JavaScript Reference**엔 다양한 예제와 정보가 있습니다.
- 위치: 2-manuals-specifications/article.md:20
- 설명: 괄호 안 'Mozilla'를 '운영하는' 관형절로 풀어 표제어 앞에 배치. 한국어의 수식어-피수식어 순서에 맞춤.

### [B] 열거 항목에 생략된 주어를 복원해 앞세움
- 원문: Again, dictionary comparison, first char `"2"` is greater than the first char `"1"`.
- 번역: 두 피연산자는 문자열이므로, 사전순으로 비교가 이뤄집니다. 왼쪽 피연산자의 첫 번째 글자 `"2"`는 오른쪽 피연산자의 첫 번째 글자 `"1"`보다 큽니다.
- 위치: 09-comparison/1-comparison-questions/solution.md:17
- 설명: 원문의 압축된 명사구 나열을 '전제(피연산자는 문자열)→결과' 완전한 문장으로 복원하고 '왼쪽/오른쪽 피연산자'로 위치를 명시. 바로 앞 항목(:16)은 간결하게 두면서 이 항목만 풀어써 리듬을 준다.

---

## G. 코드 요소 처리

### [G] 코드 주석을 문맥 설명으로 보강 번역
- 원문: `// 20 lines of code working with elem` / `// 20 more lines, now working with the clone of the elem!`
- 번역: `// 매개변수로 받아온 elem을 이용한 코드` / `// elem의 복제(clone)본을 이용한 코드`
- 위치: 04-ninja-code/article.md:155-159
- 설명: '20 lines'라는 분량 정보를 버리고 '매개변수로 받아온', '복제본을 이용한'처럼 코드의 의도를 설명하는 주석으로 재작성. 주석 안 강조는 원문의 클론 개념을 병기(clone)로 처리.

### [G] smart/warn/quote 헤더 번역의 비일관성
- 원문: ```smart header="Multi-line input"
- 번역: ```smart header="Multi-line input" (미번역)
- 위치: 4-devtools/article.md:36
- 설명: 같은 문서 내 다른 smart 헤더(1-intro의 '왜 자바스크립트인가요?', '엔진은 어떻게 동작하나요?')는 번역했으나 이 헤더만 영문 유지. 헤더 번역이 문서·역자에 따라 들쭉날쭉함을 보여주는 사례(규칙화 시 주의).

### [G] 이미지 캡션·에러 메시지 원문 유지
- 원문: not defined / Same Origin Policy
- 번역: 정의되지 않았다(not defined) / 동일 출처 정책(Same Origin Policy)
- 위치: 4-devtools/article.md:29, 1-intro/article.md:73
- 설명: 콘솔에 실제로 뜨는 문구와 고유 용어는 한글 풀이 뒤 괄호에 원문 병기. 관찰 다수.

---

## I. 담화 연결

### [I] 인과 접속어를 문미 어미로 삽입
- 원문: It does not provide low-level access to memory or the CPU, because it was initially created for browsers which do not require it.
- 번역: 메모리나 CPU 같은 저수준 영역의 조작을 허용하지 않습니다. 애초에 이러한 접근이 필요치 않은 브라우저를 대상으로 만든 언어이기 때문이죠.
- 위치: 1-intro/article.md:46
- 설명: because절을 별도 문장으로 떼고 '~때문이죠'로 인과를 명시(패턴 A+I). '-죠' 리듬 어미로 설명 톤을 살린다. 관찰 12회.

### [I] 대조 관계를 '그런데/하지만'으로 문두 표지
- 원문: But in the browser, users don't see errors by default.
- 번역: 그런데 브라우저는 스크립트에 문제가 있어서 에러가 발생해도 이를 사용자에게 직접 보여주지 않습니다.
- 위치: 4-devtools/article.md:5
- 설명: 'But'을 '그런데'로 옮기며 원문에 없는 '스크립트에 문제가 있어서 에러가 발생해도'를 보강(패턴 H)해 대조의 맥락을 채운다.

---

## 명문 규칙 확인 (빈도만 집계)

- **C. 인칭대명사 생략**: we/you/it 생략 또는 지시대상 명시. 전 파일에서 관찰(예: "우리는" 미출현, "당신"은 ninja 문서의 캐릭터 호칭으로만 의도적 사용).
- **E. 합니다체·청유형·-죠**: 전 파일. '~해봅시다'(살펴봅시다, 열어봅시다) 다수, '-죠' 리듬 어미 다수, 과한 '-시-' 없음.
- **F. 쌍점 제거**: 원문 문장 끝 콜론(`:`)을 마침표·'다음과 같습니다'로 대체. 10회 이상. 리스트 라벨 뒤(예: '예시:')는 유지.
- **F. 작은따옴표**: 강조는 '안전한', '동생', '검색' 등 작은따옴표. 큰따옴표는 실제 인용/에러문구에만.
- **D. 한-영 병기**: 스크립트(script), 트랜스파일(transpile, 변환), 명세서(specification) 등 핵심 용어 첫 등장 병기. 15회 이상.
- **F. 가운뎃점**: 이 청크에서는 뚜렷한 짝 단어 사례 적음(대·소문자 류 미출현).
