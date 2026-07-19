# it-docs-translation-ko 설계 (범용 IT 문서 번역 스킬)

날짜: 2026-07-19 · 결정자: 이보라

## 목적

tech-translation-ko는 javascript.info 기여에 특화되어 있다(줄 수 보존 계약, JS 용어집,
하우스 스타일). 같은 번역 기법을 도메인 제약 없이 쓰는 범용 스킬을 분리한다.

## 결정 사항

- **위치**: 같은 저장소의 병렬 스킬 `skills/it-docs-translation-ko` (새 저장소 대신).
  스크립트·분석 근거를 공유하고 배포도 한 저장소에서 한다.
- **이름**: `it-docs-translation-ko`
- **스크립트**: check_translation.py·glossary_lookup.py·nara_speller.py를 바이트 동일
  복사본으로 둔다(스킬 설치 시 자기완결성 필요). 갱신 시 두 스킬을 함께 맞춘다.

## 범용화 델타 (tech-translation-ko 대비)

1. 구조 계약(줄 수 = 원문)은 기본 off. diff 동기화 프로젝트만 opt-in (`--source`).
2. 용어집은 bring-your-own. 기본 용어집을 싣지 않고 docs/analysis의 두 TSV를
   스타터로 안내한다.
3. 하우스 스타일 제거: 예제 인명 현지화·에러 문자열 치환·`<info:>` 링크·smart 블록
   등은 '프로젝트별 결정 사항'으로 일반화.
4. 예시 현지화 수위: 공식 문서·API 레퍼런스는 원문 유지가 기본, 튜토리얼·블로그만 재량.
5. review-checklist에서 PR 번호 등 js-info 실사례 참조를 일반 서술로 대체하고
   '하우스 스타일 결정 이력' 절을 신설.
6. references의 principles·terminology·kigo-conventions·examples는 이미 도메인 중립이라
   그대로 복사(examples는 CC BY-NC 출처 표기 유지).

## 비범위

- 두 스킬의 공통 문서를 단일 소스로 합치는 빌드 체계(현 규모에선 과잉 설계)
- 도메인별 스타터 용어집 추가 제작
