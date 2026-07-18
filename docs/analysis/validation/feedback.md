# skill 검증 결과와 반영 내역

clean-room 검증: 검증 에이전트가 한국어 번역본을 보지 않고 skill 문서만으로
`1-js/11-async/07-microtask-queue/article.md`(en 112줄)를 번역했다. 결과는
`skill_translation.md`(112줄, 줄 수 보존, 린터 0 error). 원 번역과 구조 완전 일치,
표현 차이는 112줄 중 43줄.

## 발견된 skill 결함과 반영

1. 헤딩 병기 규칙 충돌(terminology '첫 등장 병기' vs checklist '헤딩 병기 제거')
   → terminology.md·sentence-patterns.md에 '병기는 본문에서, 헤딩엔 금지' 명문화
2. Error/throw 인자 문자열의 번역 여부 미정의 → formatting.md에 경계선 명문화.
   교정 코퍼스 근거(Whoops!→에러 발생! 약 10회)로 '예제가 정의하는 문자열은 번역,
   언어가 생성하는 에러 출력만 원문 유지'로 확정
3. 코드 문자열-본문 참조 반쪽 현지화가 린터 사각 → formatting.md·review-checklist.md에
   grep 확인 스텝 추가
4. 용어집 이탈 판단 기준 부재(task=과제 vs 비동기 task=작업) → terminology.md에
   'Deviating from the glossary' 절 신설(합성어·도메인 스코프, 의도적 이탈은 기록)
5. '등재 후 번역'이 일회성 작업에 비현실적 → read-only 용어집 모드('결정 기록 후
   번역') 추가
6. 단순 개념명 헤딩 과잉 편집 위험 → sentence-patterns.md #8에 '개념명 헤딩은 직역,
   동작형 강제 금지' 추가
7. 화면 문자열 중의성('잡음') → formatting.md에 주의 추가
8. KO-W003 오탐 3/3(제품명 Node.js, 병기 원어, 대체 역어 미인식) → 린터 개선:
   단어 경계에 `.js`류 제외, 한-영 병기 괄호 구간 제외, 쉼표·슬래시 대체 역어 전체
   확인. 재검사 결과 warning 3→1(잔여 1건은 정당한 회색 지대)
