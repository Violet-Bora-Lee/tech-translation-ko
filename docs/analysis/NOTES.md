# 분석 주의사항·데이터 계보 노트

## 저자 매칭

지시된 이름 리터럴 3개(Violet Bora Lee, Bora Lee, Violet.Lee) 외에 동일 이메일로 확인된
표기 변형 4개(Bora Lee (Violet), Violet-Bora-Lee, 이보라, DESKTOP-3VC7VHH\learn)를 포함해
총 7개 변형을 매칭했다. 리터럴 3개만 매칭하면 808개 커밋 중 약 12%가 누락된다.
이메일은 매칭에만 사용하고 산출물엔 기록하지 않았다.

## blame 비율 해석 주의

new_translation(blame 0.7 이상) 15건은 과소집계다. 이후 영어 원문 동기화 병합과 타인
교정이 blame을 희석시키기 때문이다. 패턴 분석은 blame 0.4 이상 76개 파일을 대상으로 했고,
'이보라 커밋 시점 diff' 기준이 더 정확한 귀속이다(manifest.json의 커밋 목록 참고).

## 정렬 전제가 깨지는 파일

- `1-js/03-code-quality/06-polyfills/article.md`: ko 55줄 vs en 90줄. ko는 구버전 원본을
  번역한 것으로 이후 en이 개편됨. 줄 단위 정렬 불가, H(보강) 판정에서 제외했다.
- 유사 사례 가능성이 있으므로 대조 전 줄 수·헤딩 대응을 선행 확인해야 한다.

## 골든 데이터 구축 시 제외 대상

- 미번역: `7-animation/2-css-animations/2-animate-logo-bezier-css/solution.md`(전문),
  `2-ui/1-document/11-coordinates/2-position-at/task.md`(전문),
  `8-web-components/index.md`(본문)
- 오역: `2-ui/3-event-details/1-mouse-events-basics/article.md` clientX/Y↔pageX/Y 설명 역전,
  `1-js/11-async/07-microtask-queue/article.md` "V8 term"→"ES8 용어",
  bezier-curve smart header '조절점은 통과하는'(주체 어긋남)
- 오타: `find-elements/solution.md` 2건('찾교', 'from을'), bezier-curve 표기 2건

## 분석 일관성 검증

청크 2를 두 에이전트가 독립 분석한 결과(chunk-2.md, chunk-2-dup.md) 핵심 사례
(이보라 이름 현지화, 열거 명시화, 담화 마무리 보강, alert 주석 서술화)와 카테고리 빈도가
일치해 코드북 적용 일관성을 확인했다.
