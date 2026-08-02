# Design Brief — 문대한 서비스 기획 포트폴리오

**대상**: https://moondh99.github.io · repo `moondh99/moondh99.github.io`
**로컬 워킹카피**: `/Users/moondh/Desktop/자기소개서/portfolio/`
**형식**: 단일 파일 정적 HTML (`index.html`, 인라인 `<style>` + 인라인 `<script>`). 빌드 없음. Next.js/React 아님 — GitHub Pages가 파일 그대로 서빙.

> **토큰의 진실 공급원은 `portfolio/index.html` 의 `:root` 블록 (15–53행)이다.**
> 이 문서는 그 값의 명세이자 사용 규칙. 별도 `design-tokens.css` 는 두지 않는다 (import 하는 곳이 없는 죽은 파일이 됨).
> **모든 태스크는 아래 정의된 값만 사용한다. 새 색상·폰트·간격 값 임의 생성 금지.**

---

## 1. 톤앤매너

**차분한 에디토리얼 · 증거 우선 · 고밀도.**

- **채용담당자 3초 룰**: 스크롤 없이 ① 이름·직무 ② 한 줄 논지 ③ 정량 지표 4개가 다 읽힌다.
- **모든 주장에 근거를 붙인다.** 이 포트폴리오의 핵심 장치는 "주장 → `근거` 블록" 패턴이다 (`.evidence`, `.pm-note`, `.i-src`). 근거 없는 형용사 금지.
- **수치는 mono 폰트 + accent 색 + `tabular-nums`.** 지면에서 숫자가 먼저 눈에 띄어야 한다.
- 장식 금지: 그라디언트, 스톡 이미지, 아이콘 세트, 패럴랙스 없음. 활자·1px 선·여백만으로 위계를 만든다.
- **라벨은 mono + uppercase + `letter-spacing:.06em`**, 본문은 Pretendard. 이 두 축의 대비가 시각적 정체성이다.
- 모션은 존재감 없어야 함. 진입 시 1회 `rise` (300ms), 임팩트 바 `scaleX` (600ms). 그 이상 추가 금지.

---

## 2. 컬러 팔레트

`index.html:15-53`. 라이트/다크 + `prefers-color-scheme` + `[data-theme]` 오버라이드.

| 토큰 | Light | Dark | 용도 |
|---|---|---|---|
| `--paper` | `#f7f7f5` | `#121614` | 페이지 배경 |
| `--card` | `#ffffff` | `#1a201d` | 카드 배경 (`.case` `.proj` `.impact` `.mini`) |
| `--ink` | `#1d2320` | `#e7ebe8` | 본문·헤드라인 |
| `--sub` | `#5b645f` | `#a4ada7` | 보조 설명·리드 |
| `--faint` | `#67706a` | `#8b958f` | 메타(기간·출처)·캡션 |
| `--line` | `#e3e6e2` | `#2a322e` | 1px 구분선·보더 |
| `--accent` | `#0e6e5c` | `#3fbba0` | 라벨·링크·정량 수치·포커스 링 |
| `--accent-soft` | `#e3f0ec` | `#1c2f2a` | 배지·스텝 번호·델타 배경 |
| `--chip-bg` | `#eef1ee` | `#232a26` | 칩·플로우 노드 배경 |
| `--quote` | `#3d4642` | `#c3cbc6` | `blockquote` 전용 |

**액센트는 딥 그린 단색 1개.** 색을 추가하지 않는다 — 상태 표현이 필요하면 굵기·크기·여백으로 푼다.

### 명도 대비 (실측, WCAG 2.1)

| 조합 | Light | Dark |
|---|---|---|
| `--ink` on `--paper` | 14.90 AAA | 15.16 AAA |
| `--sub` on `--paper` | 5.70 AA | 7.92 AAA |
| `--faint` on `--paper` | 4.77 AA | 5.90 AA |
| `--accent` on `--paper` | 5.75 AA | 7.67 AAA |
| `--ink` on `--card` | 15.99 AAA | 13.76 AAA |
| `--faint` on `--card` | 5.12 AA | 5.36 AA |
| `--accent` on `--card` | 6.17 AA | 6.96 AA |
| `--accent` on `--accent-soft` | 5.27 AA | 5.93 AA |
| `--ink` on `--chip-bg` | 14.05 AAA | 12.19 AAA |

**금지 조합** (본문 4.5:1 미달):
- `--faint` on `--accent-soft` → 4.37 ✗
- `--faint` on `--chip-bg` → 4.50 (라이트에서 경계값) ✗

`--line` 은 대비 1.17로 **장식용 구분선 전용**. 정보를 전달하는 경계(입력 필드 테두리 등)에 쓰지 않는다.

---

## 3. 타이포

```
--mono: ui-monospace, "SF Mono", Menlo, "Cascadia Mono", "D2Coding", Consolas, monospace
본문: "Pretendard Variable", Pretendard, -apple-system, BlinkMacSystemFont,
      "Apple SD Gothic Neo", "Noto Sans KR", "Segoe UI", sans-serif
```

**웹폰트 로드 없음** — Pretendard는 로컬 설치본만 사용하고 없으면 시스템 한글 폰트로 폴백. 네트워크 요청 0. 이 결정을 뒤집지 말 것.

### 허용 크기 (이 값 외 사용 금지)

| px | 용도 |
|---|---|
| 12 | mono 라벨(`eyebrow` `phase` `f-role` `ev-k`), 메타, 캡션 |
| 13 | `h2` 섹션 라벨, 칩, 타임라인 항목, `evidence` |
| 14 | 연락처, `pm-note`, `.impact h4`, 스킬 |
| 15 | 리스트 본문(`xp-item li`), 스토리 본문, `.pa` |
| 16 | 기본 본문 (`body`) |
| 17 | `.step h3`, `.xp-item h3` |
| 19 | `.proj h3` |
| `clamp(19px,2.8vw,23px)` | Hero 논지, `.case-head h3` |
| `clamp(20px,3vw,25px)` | `.sec-lead` |
| `clamp(22px,3.4vw,28px)` | `#case .sec-lead` |
| `clamp(30px,5vw,42px)` | `h1` |

### 규칙

- **한글 본문 `line-height:1.7` 고정.** 영문 기준 1.5 쓰지 말 것. 제목은 1.25–1.55.
- 웨이트는 **500 / 700 / 800** 세 단계만. 400은 `body` 기본값으로만.
- `letter-spacing`: mono 라벨 `.06em` (또는 `.02em`/`.04em`), 큰 제목 `-.01em`. 본문은 기본값.
- `word-break:keep-all` + `overflow-wrap:break-word` — 한글 어절 단위 줄바꿈. 제거 금지.
- `text-wrap:balance` (제목) / `pretty` (본문) 유지.
- 모든 숫자에 `font-variant-numeric:tabular-nums`.
- **본문 최대폭**: `.wrap` 800px. 본문 문단은 `max-width:66ch`, Hero 논지 `44ch`, blockquote `60ch`.

---

## 4. 여백 / 레이아웃

- 컨테이너 `.wrap` = `max-width:800px`, 좌우 패딩 24px. **이 폭이 에디토리얼 톤의 핵심** — 넓히지 말 것.
- 섹션 세로 여백 `52px 0`, 하단 `1px solid var(--line)`, 마지막 섹션은 보더 없음.
- Hero `72px 0 48px`.
- 카드 패딩: `.case` 30px, `.proj` 26px, `.impact` 18px, `.mini` 16px. 600px 이하에서 `.case`/`.proj` → `22px 18px`.
- **허용 간격값**: 2 / 4 / 6 / 8 / 10 / 12 / 14 / 16 / 18 / 20 / 22 / 24 / 26 / 30 / 34 / 36 / 44 / 48 / 52 / 64 / 72. 이 밖의 값 신규 사용 금지.
- radius: 카드 16px, 중간 12px, 작은 요소 8px, 배지 999px.
- `--shadow-card` 만 사용. 새 그림자 정의 금지. hover 시 그림자 변경 없음.

### 그리드 패턴 (기존 사용 중, 재사용할 것)

```css
repeat(auto-fit, minmax(150px, 1fr))   /* .stats, .tl */
repeat(auto-fit, minmax(240px, 1fr))   /* .mini-grid */
repeat(auto-fit, minmax(250px, 1fr))   /* .impact-grid */
150px 1fr   /* .xp-item  — 600px 이하 1fr */
130px 1fr   /* .skill-row — 600px 이하 1fr */
36px 1fr    /* .step */
64px 1fr    /* .pa */
1fr 1fr     /* .two-col — 600px 이하 1fr */
```

**브레이크포인트는 `max-width:600px` 하나뿐.** 새 브레이크포인트 추가 전에 `auto-fit`/`clamp()`로 풀 수 있는지 먼저 확인.

---

## 5. Hero

현재 카피 (**유지**):

> **문대한** / 데이터를 이해하는 서비스 기획자
> "어떻게 만들 것인가"보다 **"왜 기존 방식이 실패하는가"**를 먼저 묻습니다. 문제를 유형으로 구조화하고, 이견은 데이터로 좁히고, 성과는 지표로 증명해 온 10여 개 프로젝트의 기록입니다.

지표 4개: `10+` 프로젝트 · `대상 2회` · `15% → 0.8%` · `500,000+`

구조: `eyebrow(mono) → h1 → role → thesis → contact → stats`. 순서 고정.

---

## 6. 실제 콘텐츠 인벤토리

> ⚠️ 초안에 있던 "프로젝트 A/B/C" 매핑은 구 이력서 PDF 기준이라 **폐기**. 실제 구성은 아래.

**섹션 순서**: Journey → Process → Case Study → Numbers → Experience → Featured Projects → More Work → How I Work → Skills & Awards → footer

**Featured Projects (4건)**

| # | 프로젝트 | 역할 | 핵심 수치 |
|---|---|---|---|
| 1 | Dear Log — AI 인터뷰 기반 가족 기억 아카이브 | 캡스톤 6인 팀, 기획·개발 | 캡스톤 **대상**, dear-log.com 실배포, 목적별 동의 5종 |
| 2 | 멀티 AI 공약 이행 검증 파이프라인 | 갭이어, 기획·파이프라인 설계 | 처리 속도 −80%, 할루시네이션 −15% |
| 3 | 유가증권 투자 애널리스트 AI | 한이음 5인 팀 **팀장/PM** | 예측 정확도 +12%, 검수 −30%, 개발 기간 −20% |
| 4 | 따릉이 수요 예측 · 운영 최적화 | 한이음 4인 팀 **팀장** | 처리 시간 −85%, 예측 오차 −18%, 일 20만 건 |

**Case Study (1건, 별도 취급)**: 경기도 문화시설 접근성 분석 — 연구랩업 **대상**, 3인 팀 팀장. 5단계 서사 이미 구축됨.

**More Work (5건)**: 미래에셋 교육 플랫폼 기획 / K리그 예측 / LG Aimers MQL / 수강신청 개편 설계 / KBI 카드뉴스

---

## 7. 접근성 기준

**유지 중 (건드리지 말 것)**

- `prefers-reduced-motion` — `scroll-behavior`, `.stat` rise, `.i-bar` scaleX 전부 차단
- `prefers-color-scheme` 다크 대응
- `:focus-visible` — `outline:2px solid var(--accent); outline-offset:2px`
- `.flow li::after` 의 `content:"→" / ""` — 화살표에 빈 대체 텍스트 부여 (스크린리더 무시)
- `.step .num` `aria-hidden="true"` + CSS counter
- `a:hover` 를 `@media (hover:hover) and (pointer:fine)` 로 가드
- 외부 링크 `rel="noopener"`
- 단일 `h1`, `h2 → h3 → h4` 위계 유지

**Task 3 점검 항목**

- [ ] skip-to-content 링크 없음 → 추가
- [ ] `<section>` 에 `aria-labelledby` 없음 → `h2` 에 `id` 부여 후 연결
- [ ] 터치 타깃 44×44px 미만 요소 확인 (`.contact` 인라인 링크, footer 링크)
- [ ] `[data-theme]` 셀렉터는 있으나 **토글 UI가 없음** → 토글 추가하거나 죽은 CSS 제거 (둘 중 하나, 방치 금지)
- [ ] `.i-bar` 임팩트 막대가 순수 시각 요소 — 수치가 텍스트로 병기돼 있는지 재확인
- [ ] `.tl-col::before/::after` 장식 요소가 스크린리더에 노출되지 않는지 확인
- [ ] 600px 미만 / 320px 폭에서 `.flow` 가로 넘침 확인
- [ ] 명도 대비 §2 표 유지, §2 금지 조합 신규 사용 여부 검사

---

## 8. 태스크 게이트

- [x] **Task 0** — 디자인 브리프 확정 (이 문서). 토큰 = `portfolio/index.html:15-53`
- [ ] **Task 1** — Claude Code: Featured Projects 4건 서사를 **문제 정의 → 리서치/가설 → 기획 프로세스 → 결과/정량 임팩트** 순으로 재구성 (현재 `.pa` = 문제/접근/결과 3단)
- [ ] **Task 2** — Codex: Selected Projects 카드 리스트 레이아웃 + About/Skills/Contact 섹션
- [ ] **Task 3** — Antigravity: 반응형 + 접근성(§7 체크리스트) + 브리프 이탈 스타일 교정

> ⚠️ **Task 1·2 병렬 불가**: 전체가 `index.html` 단일 파일이고 두 태스크 모두 `#projects` 구역을 건드린다. 순차 실행한다.
