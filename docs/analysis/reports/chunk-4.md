# 청크 4 대조 분석 리포트

## 개요

- 분석 파일 수: 3
  - `7-animation/1-bezier-curve/article.md` — 완역. 실질 분석 대상.
  - `7-animation/2-css-animations/2-animate-logo-bezier-css/solution.md` — **미번역**(en과 ko 바이트 단위로 동일).
  - `8-web-components/index.md` — **부분 번역**. 제목 `# Web components → # 웹 컴포넌트`만 번역, 본문 한 문단은 영어 원문 그대로.
- 실질 대조 가능 파일: 1편(bezier-curve). 아래 패턴은 전부 이 파일에서 추출했다.

### 카테고리별 관찰 빈도

| 카테고리 | 관찰 빈도 | 비고 |
| --- | --- | --- |
| A. 문장 분해·재구성 | 9 | dash 구조 해체가 특히 반복 |
| B. 어순·정보구조 재배치 | 4 | 알고리즘명 후치→관형절 전치가 대표 |
| C. 인칭·대명사 처리 | 7 | 주어 명시(조절점의 개수는 등)와 it→대상 명시 |
| D. 어휘 선택·용어 | 6 | 음차(카스텔조), 한-영 병기, 유의어 변주 |
| E. 어미·문체 | 8 | 합니다체 본문 / 한다체 요약 불릿 혼용 |
| F. 문장부호·표기 | 6 | 쌍점 제거, 큰따옴표→작은따옴표 |
| G. 코드 요소 처리 | 3 | 색상 span 유지, smart header 번역 |
| H. 생략·보강 | 9 | 정의 보강 · smart 블록 통째 생략 |
| I. 담화 연결 | 4 | 인과·대조 접속어 추가 |
| J. 신규 패턴 | 3 | 미번역 파일, 병렬 구문 변주, 번역 슬립 |

---

## 상세 패턴

### [H] 정의를 원문에 없던 수식으로 보강
- 원문: Bezier curves are used in computer graphics to draw shapes, for CSS animation and in many other places.
- 번역: 베지어 곡선(Bezier Curve)은 컴퓨터 그래픽스에서 사용되는 특별한 형태의 곡선으로, CSS 애니메이션 등에서 도형을 그릴 때 사용합니다.
- 위치: 7-animation/1-bezier-curve/article.md:3
- 설명: 원문에 없는 '특별한 형태의 곡선으로'라는 정의성 동격을 삽입해 첫 문장만 읽어도 대상이 무엇인지 잡히게 했다. 동시에 `in many other places`를 '등'으로 압축하는 생략과 짝을 이룬다.

### [H] smart 안내 블록 전체 생략
- 원문: ```smart header="Some theory, please" … Please take your time to read and understand the concept, it'll serve you well.``` (article.md:7-11)
- 번역: (해당 블록 없음)
- 위치: 7-animation/1-bezier-curve/article.md:5→7 사이
- 설명: '이론이 좀 필요하다'는 메타 안내 smart 블록을 통째로 들어냈다. 다음 글로 넘어가는 안내와 독려 문장이라 본문 이해에 필수가 아니라고 판단한 것으로 보인다. 기계 규칙으로 잡기 어려운 편집 재량 생략의 대표 사례.

### [C] 무주어·대명사 문장에 주어를 세워 명시
- 원문: There may be 2, 3, 4 or more.
- 번역: 조절점의 개수는 2개나 3개, 4개가 될 수 있고 이보다도 많을 수 있습니다.
- 위치: 7-animation/1-bezier-curve/article.md:11
- 설명: 영어 존재구문(There may be)을 '조절점의 개수는'이라는 주어로 되살려 앞 문장과의 연결을 끊기지 않게 했다. 같은 기법이 `They are a very simple thing → 곡선 자체는`(article.md:5), `it'll serve you well` 계열에서도 반복(관찰 7회).

### [A] 명사구 캡션을 청유형 완결 문장으로 전환
- 원문: For instance, two points curve:
- 번역: 조절점이 두 개인 베지어 곡선을 살펴봅시다.
- 위치: 7-animation/1-bezier-curve/article.md:13
- 설명: 그림 앞 라벨(명사구+쌍점)을 '~살펴봅시다'는 완결 문장으로 바꿔 이미지와 본문의 호흡을 이었다. 쌍점 제거(F)와 동시에 일어난다.

### [D] 병렬 구문을 일부러 서로 다른 문형으로 변주
- 원문: For instance, two points curve: / Three points curve: / Four points curve:
- 번역: 조절점이 두 개인 베지어 곡선을 살펴봅시다. / 조절점이 세 개인 베지어 곡선은 다음과 같습니다. / 네 개의 조절점이 있을 땐 다음과 같은 곡선이 나옵니다.
- 위치: 7-animation/1-bezier-curve/article.md:13, 17, 21
- 설명: 영어는 동일 구조 세 번 반복이지만, 번역은 '~살펴봅시다 / ~다음과 같습니다 / ~곡선이 나옵니다'로 문형을 셋 다 다르게 썼다. 단조로움을 피하려는 의도적 유의 변주로, 기계 치환으로는 나오지 않는 암묵지.

### [B] 후치된 알고리즘명을 관형절로 끌어올려 전치
- 원문: There's a mathematical formula for Bezier curves, but let's cover it a bit later, because [De Casteljau's algorithm] is identical to the mathematical definition and visually shows how it is constructed.
- 번역: 베지어 곡선을 정의하는 수학 공식은 나중에 살펴보고, 그 전에 베지어 곡선을 정의하는 공식과 정확히 일치하고 곡선이 만들어지는 과정을 시각화할 때 도움을 주는 [카스텔조 알고리즘]에 대해 알아봅시다.
- 위치: 7-animation/1-bezier-curve/article.md:52
- 설명: 영어는 알고리즘명을 먼저 놓고 설명을 뒤에 붙이지만, 번역은 설명 전체를 관형절로 만들어 '카스텔조 알고리즘' 앞에 배치했다. 두 문장(58-59행)을 하나로 합치는 A와도 결합. 한국어의 수식어-피수식어 순서에 맞춘 전형적 정보 재배치.

### [H] 어려운 용어를 풀어쓰며 보강
- 원문: **As you can notice, the curve stretches along the tangential lines 1 -> 2 and 3 -> 4.**
- 번역: 예시를 통해 **베지어 곡선이 조절점을 이은 선(1-2, 3-4)을 향해 뻗어나가는 것을 확인할 수 있습니다.**
- 위치: 7-animation/1-bezier-curve/article.md:42
- 설명: `tangential lines`(접선)라는 용어를 그대로 쓰지 않고 '조절점을 이은 선'으로 풀어 독자가 그림과 바로 대응시키게 했다. `As you can notice`도 '예시를 통해 ~확인할 수 있습니다'로 재구성.

### [A] em-dash로 이어붙인 강조 문장을 완결 서술문으로 해체
- 원문: **The main value of Bezier curves for drawing -- by moving the points the curve is changing *in intuitively obvious way*.**
- 번역: **조절점을 움직이면 베지어 곡선은 직관적으로 봤을 때 아주 당연한 방식으로 다시 그려집니다.**
- 위치: 7-animation/1-bezier-curve/article.md:36
- 설명: dash로 명사구와 절을 병치한 영어 강조문을 '조절점을 움직이면 ~다시 그려집니다'라는 조건-결과 완결문으로 다시 짰다. `is changing`을 '다시 그려집니다'로 능동화. dash 해체는 이 파일에서 최소 3회(article.md:36, 151, 158 계열).

### [A][H] 예시 나열을 여러 문장으로 쪼개며 압축 지시어를 구체화
- 원문: For instance, for `t=0` -- both points will be at the beginning of segments, and for `t=0.25` -- on the 25% of segment length from the beginning, for `t=0.5` -- 50%(the middle)...
- 번역: 예를 들어 설명하면 다음과 같습니다. `t`가 `0`일 땐 두 점이 선분의 시작인 조절점 1과 2에 위치합니다. `t`가 `0.25`일 땐 조절점 1에서 조절점 1과 2를 이은 선분의 길이에 25%를 곱한 값만큼 떨어진 곳에 점이 위치합니다...
- 위치: 7-animation/1-bezier-curve/article.md:72
- 설명: dash로 이어진 한 문장을 `t`값별 개별 문장으로 분해하고, 'the beginning of segments'를 '선분의 시작인 조절점 1과 2'로, 'segment'를 '조절점 1과 2를 이은 선분'으로 구체화해 계산 과정을 놓치지 않게 했다.

### [I] 문장 사이 대조·인과를 접속어로 명시
- 원문: That was a process for 3 points. But the same is for 4 points.
- 번역: 지금까진 조절점이 3개인 경우를 살펴보았는데, 조절점이 4개일 때 역시 같은 방식으로 곡선이 만들어집니다.
- 위치: 7-animation/1-bezier-curve/article.md:85
- 설명: 두 문장을 '~살펴보았는데, ~역시'로 연결해 전환을 매끄럽게 했다. `As the algorithm is recursive → 재귀성을 띄는 알고리즘 덕분에`(article.md:136), `Because of that last property → 마지막 특성 덕분에`(article.md:34)처럼 인과를 '덕분에/때문입니다'로 드러내는 사례가 반복(관찰 4회).

### [E] 담화 리듬 어미('-죠', '당연히') 삽입
- 원문: … using 5, 6 or more control points.
- 번역: … 조절점이 5개, 6개 혹은 그 이상 있는 곡선을 만들 수 있죠.
- 위치: 7-animation/1-bezier-curve/article.md:136
- 설명: 원문에 없는 '-죠' 어미로 독자에게 말 거는 리듬을 넣었다. article.md:83의 '당연히 점도 계속 추가됩니다'도 원문 `every value of t adds a point`에 없던 태도 부사를 더한 같은 계열.

### [E] 본문은 합니다체, 요약 불릿은 한다체로 문체 전환
- 원문: We can draw smooth lines with a mouse by moving control points.
- 번역: 마우스만으로 부드러운 곡선을 그릴 수 있다.
- 위치: 7-animation/1-bezier-curve/article.md:193
- 설명: 본문 전체는 '~합니다'체인데 요약 섹션의 불릿(193-194행)만 '~있다'는 한다체로 떨어뜨렸다. 요약 항목을 간결한 개조식으로 처리하는 문체 스위치로, 한 글 안에서 위치별 어미 정책이 다름을 보여준다.

### [F] 강조·인용부호 규칙 적용
- 원문: … can give a very fast "no intersection" result.
- 번역: … 아주 빠르게 곡선 역시 '교차하지 않는다'는 결론을 도출해 낼 수 있습니다.
- 위치: 7-animation/1-bezier-curve/article.md:34
- 설명: 강조성 큰따옴표를 작은따옴표로 교체(wiki 명문 규칙). smart header의 이탤릭 `*through*`도 '통과하는'으로 작은따옴표 강조 전환(article.md:138). 쌍점 문장 종결 제거는 이미지 라벨 6곳에서 반복.

### [G] 색상 span과 iframe·smart 마커는 원형 유지, 내부 텍스트만 번역
- 원문: On each <span style="color:#825E28">brown</span> segment we take a point …
- 번역: <span style="color:#825E28">갈색</span>으로 표시한 각 선분의 시작점에서 …
- 위치: 7-animation/1-bezier-curve/article.md:70
- 설명: HTML 색상 span, `[iframe src=...]`, ```online / ```smart 펜스는 손대지 않고 감싼 텍스트만 번역했다. `color:red>빨간점` 등 span 안 라벨은 문맥에 맞춰 '빨간점'으로 통일.

### [J] 청크 내 미번역·부분 번역 파일 존재
- 위치: 7-animation/2-css-animations/2-animate-logo-bezier-css/solution.md(전문 미번역), 8-web-components/index.md:3(본문 미번역)
- 설명: solution.md는 en과 완전히 동일해 번역이 시작되지 않았고, web-components 인덱스는 제목만 번역되고 본문 정의 문장은 영어 그대로다. 짧은 solution·상위 index 파일이 번역 우선순위에서 밀려 방치되는 경향을 시사한다. 패턴 추출이 아니라 커버리지 현황으로 기록.

### [J] 번역 슬립(원문 의미 이탈) 관찰
- 원문: How to draw a curve *through* given points?
- 번역: 조절점은 '통과하는' 곡선은 어떻게 그리나요?
- 위치: 7-animation/1-bezier-curve/article.md:138
- 설명: 'given points(주어진 점들)를 통과하는'이 '조절점은 통과하는'으로 옮겨져 주체가 어긋났다(조사 '은'도 중복). 본문(138행 아래)에서는 '몇몇 점을 통과하는 곡선'으로 정확히 옮겨 smart header 제목만의 국소 오류. 그 밖에 article.md:66 인용부호 짝 불일치(`... 1'`), article.md:81 `빨간점</span>)을` 잉여 괄호 같은 표기 오타 2건 관찰.
