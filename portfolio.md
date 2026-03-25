# 이현진 — Frontend Developer

> 기능 구현에 그치지 않고 시스템의 동작 원리를 이해하며
> 아키텍처 설계, 성능 최적화, 배포 자동화까지 주도한 프론트엔드 개발자

- **Email** ckeh08270827@gmail.com
- **Phone** 010-7607-9182
- **GitHub** github.com/bookhabit
- **Portfolio** bookhabit.github.io

---

## 경력

### 주식회사 비즈비 — Frontend Developer
`2024.05 – 현재`

---

#### 복지찬스 APP `2025.08 – 현재`

---

##### 만보기 서비스 구현 및 포인트 지급 제도로 MAU 300% 증가

**문제**
단순 걸음수 측정만으로는 사용자 재방문 유도 미흡

**해결**
- 차등 보상 시스템: 일일 목표 달성도에 따른 복지 포인트 즉시 지급
- 광고 리워드 구조: 포인트 지급 전 광고 시청으로 수익성·유저 혜택 공존
- 온/오프라인 결제 생태계: 외부 결제 모듈·가맹점 API 연동으로 포인트 실사용성 확보

**결과**
- MAU 300% 상승 (재방문율 유의미 개선)
- 포인트 적립 → 광고 시청 → 가맹점 결제까지 End-to-End 유저 저니 완성

---

##### SSOT 기반 아키텍처 재설계

**문제**
- Foreground Service 알림창 UI 추가로 알림창 UI ↔ 앱 화면 간 걸음수 불일치 발생
- JS·Native 레벨 싱크 코드 중복으로 관리 불가 상태

**해결**
- **Native Layer**: `StepCounterManager` 싱글톤 도입, Service·Module은 매니저를 구독하는 형태로 관심사 분리
- **JS Layer**: `useSyncExternalStore` 도입으로 고빈도 데이터를 React 렌더링 엔진과 분리
- **단방향화**: Service → DB → React Native 흐름 정리, 포그라운드 진입 시 DB 기준 UI 재동기화
- Android Native Module(AOSPedometer), Room DB·DAO·Repository 레이어 설계

**결과**
- 알림창/앱 UI 걸음수 불일치 완전 해결
- 앱 재실행·백그라운드 복귀 시에도 일관된 상태 유지
- 위젯·워치 연동 확장성 확보

---

##### 네이티브 만보기 엔진 설계 — 삼성헬스·토스 벤치마킹

**문제**
- 외부 라이브러리(Google Fit) 종속성 높음, 커스텀 리워드 로직 제약
- 기기 재부팅·강제 종료 시 누적 걸음수 초기화
- Android 12~15 배터리 최적화 정책으로 백그라운드 서비스 생존율 저하

**해결**
- Android Native Sensor API 직접 제어로 독자 엔진 설계
- 삼성헬스·토스 벤치마킹 기반 가속도 센서 고정밀 측정 로직 구현 (오차 1% 이내)
- Android Jetpack Room으로 영속성 레이어 설계, 재부팅 후에도 누적값 보존
- START_STICKY + 알림 우선순위 최적화, Android 10~15 OS별 권한 분기 처리

**결과**
- 삼성헬스·토스 대조 테스트 걸음수 오차 **1% 이내**
- 1만 명 이상 실사용 환경에서 높은 서비스 연속성 확보

---

##### Firebase Crashlytics 기반 ANR 모니터링 체계 구축

**문제**
- Crash-free 96.5% (1만 명 규모에서 위험 수준)
- Android 12+ ForegroundServiceStartNotAllowedException 등 비정상 종료·ANR 지속 발생
- Release 빌드에서만 재현되는 크래시로 로컬 디버그 환경에서 원인 특정 불가

**해결**
- 크래시 리포트에 사용자 정보 + 회원사 정보를 함께 제출하는 커스텀 리포팅 구조 설계
- Crashlytics ANR 탐지 → 스택 트레이스 분석 → Android Studio Profiler 로컬 재현 → OS 버전별 Foreground Service 정책 분기 처리

**결과**
- Crash-free **96.5% → 99.8%**
- Android 12+ ANR 발생률 0.3%대로 감소
- 장애 대응 시간 **90% 단축**

---

##### Expo SDK 마이그레이션 (v51 → v53) & New Architecture 전환

**배경**
Google Play Android 15(API 35) 타겟팅 의무화 대응 + Bridge 방식 성능 한계 극복

**해결**
- Bridge 방식 제거 → JSI(JavaScript Interface) 기반 동기식 네이티브 호출 전환
- Fabric Renderer 도입으로 복잡한 레이아웃 렌더링 효율 개선
- TurboModules 규격에 맞춘 커스텀 브릿지 코드 리팩터링
- 16KB 페이지 크기 호환성 확보: 네이티브 종속성 전수 조사 후 호환 바이너리(.so) 교체

**결과**
- Android 15 타겟팅 및 최신 Google Play 배포 규정 준수
- 네이티브 모듈 통신 지연 단축, 앱 전체 응답 속도 개선

---

##### EAS · Fastlane 기반 배포 자동화

**문제**
- 업체별 빌드 환경 수동 관리로 설정 오류·빌드 실패 빈번
- 오타 수정 등 가벼운 변경에도 스토어 심사로 수일 소요
- 스토어 콘솔 수기 업로드 등 반복 단순 작업으로 생산성 저해

**해결**
- `eas.json`으로 빌드 프로필 코드화(IaC), 클라우드 빌드로 로컬 환경 의존성 제거
- 네이티브 변경 없는 수정은 EAS Update OTA로 심사 없이 즉시 반영
- Fastlane 연동으로 바이너리 생성 → 스토어 제출 전 과정 명령어 한 줄 자동화

**결과**
- 단순 수정 배포 수일(심사 대기) → 수 분(OTA), 릴리즈 주기 **95% 개선**
- 빌드 환경 코드화로 빌드 성공률 **100%** 달성

---

#### 비즈비톡 APP `2024.09 – 2025.07`

---

##### 실시간 채팅 시스템 개발 (STOMP WebSocket & React Query)

**문제**
메시지 전송 후 서버 응답 대기로 UI 갱신 지연 → 사용자 경험 저하

**해결**
- **Optimistic Update**: `onMutate` 단계에서 새 메시지를 React Query 캐시에 즉시 삽입
- **Rollback**: 전송 실패 시 `onError`에서 `previousData`로 캐시 복구 + 재전송 버튼 노출
- **Factory Pattern**: 9종 이상 메시지 타입(텍스트·이미지·파일·멘션 등)을 `타입 → 렌더링 컴포넌트` 매핑으로 구축. OCP 준수로 신규 타입 추가 시 기존 로직 수정 불필요

**결과**
- 메시지 UI 반영 속도 **0ms** (Optimistic Update)
- 9종 이상 복합 메시지 타입 확장형 구조 완성

---

##### Non-blocking 아키텍처 — 연락처 기반 초대 시스템

**문제**
4,000건 연락처를 매번 API로 처리하는 과정에서 메인 JS 스레드 점유 → 프레임 드랍 및 25초 이상 로딩

**해결**
- **Offline-First (SQLite)**: API 결과를 로컬 SQLite에 저장, Single Source of Truth로 활용. 재진입 시 로컬 DB에서 즉시 렌더링
- **Headless JS**: 동기화 작업을 백그라운드 프로세스로 완전 분리 → 메인 스레드 점유율 0%
- **차분 동기화(Differential Sync)**: 타임스탬프 비교로 변경된 데이터(Delta)만 서버와 통신

**결과**
- 로딩 시간 25초 → **1초 이내**
- 메인 스레드 점유율 0%, 오프라인 지원, API 호출 대폭 감소

---

##### SQLite Local-First 아키텍처 및 성능 최적화

**문제**
친구 목록·프로필·채팅방을 매번 API 호출 → 서버 과부하 및 불필요한 트래픽

**해결**
- 모든 데이터 흐름 중심을 로컬 SQLite로 설정 (SSOT). 화면 진입 시 로컬 DB 즉시 조회, 백그라운드에서만 서버 Revalidation
- **Action Queuing**: 오프라인 중 인터랙션을 로컬에 임시 저장, 네트워크 복구 시 자동 동기화
- SQLite 업데이트 시 `invalidateQueries` 또는 직접 캐시 갱신으로 UI ↔ DB 일관성 유지
- SQL INDEX + SQL 레벨 페이징으로 대량 채팅 데이터 렌더링 최적화

**결과**
- 화면 초기 로딩 **1.2s → 0.1s**
- API 호출 **70% 절감**
- 네트워크 단절 시 '에러 화면' → '주요 기능 정상 동작'으로 전환

---

##### 하이브리드 알림 시스템 — WebSocket & FCM 분산 설계

**문제**
- 포그라운드 상태에서도 FCM 경유로 평균 1~3초 알림 지연
- 소켓 + FCM 중복 수신으로 서버 리소스 낭비

**해결**
- **포그라운드**: WebSocket 수신 데이터를 Notifee로 로컬 알림 즉시 표시 (외부 서버 경유 없음)
- **백그라운드**: 소켓 미연결 상태에서 서버 → FCM 전송
- 포그라운드 ↔ 백그라운드 전환 구간 알림 유실·중복 방지를 위한 알림 고유 ID 중복 체크 로직 구현

**결과**
- 포그라운드 알림 속도 1~3초 → **즉시 발생**
- 활성 사용자 대상 FCM 서버 호출 수 대폭 감소

---

##### 인증/인가 E2E 테스트 자동화 (Detox)

**문제**
1인 프론트엔드·QA 부재 환경에서 기획 변동과 서버 코드 변경 속 배포 불안정성 발생

**해결**
- Form Validation·API 에러 처리 로직을 테스트 시나리오로 고정 → 테스트 코드가 곧 기능 명세서
- 서버 코드 변경 후 E2E 실행으로 배포 전 클라이언트-서버 정합성 문제 포착
- 인증 플로우 회귀 테스트 안전망으로 리팩터링·기능 고도화 자신감 확보

**결과**
- 수동 확인 20여 개 시나리오 → 수 분 내 자동 검증
- 배포 전 정합성 문제 **100% 사전 포착**

---

##### 금융감독원 수검 대비 모바일 앱 보안 고도화 및 취약점 선제 대응

###### ① 변조 실행 환경 통제 — 루팅/탈옥 및 디버깅 차단

**배경**
루팅/탈옥 기기는 OS 보안 샌드박스가 무너져 메모리 해킹·데이터 탈취에 취약. 금융 앱 필수 보안 사항인 '실행 환경 무결성' 확보 필요.

**해결**
- 오픈소스 라이브러리(`JailMonkey` 등)에 의존하지 않고, Native(Java/Swift) 레벨에서 `su` 바이너리·`Cydia` 패키지·시스템 디렉터리 권한을 직접 체크하여 최신 우회 기법까지 대응
- 앱 최초 실행뿐 아니라 **중요 금융 거래 직전** 재검증 로직 실행으로 런타임 우회 시도까지 차단
- Release 빌드에서 디버거 연결·에뮬레이터 감지 시 즉시 앱 종료 → 동적 분석 및 로직 우회 차단

**결과**
- 변조 환경에서의 앱 실행 100% 차단
- 금감원 '비정상 단말기 이용 제한' 항목 완벽 준수

---

###### ② 역공학 방지 — ProGuard & JS Bundle 난독화

**배경**
React Native 특성상 JS 번들이 평문으로 빌드되어 비즈니스 로직·API 키 탈취 위험. JADX·apktool 등 분석 도구로 소스코드 가독성 확보 시 공격 타겟화.

**해결**
- **JS 난독화**: Metro Bundler 설정으로 배포 번들 최소화(Minify) 및 변수명 치환 적용
- **Native 보호**: Android R8/ProGuard로 Java/Kotlin 클래스·메서드명 무작위 치환 + 미사용 코드 제거(Shrinking)
- **예외 규칙 최적화**: 외부 라이브러리·네이티브 브릿지 연동 런타임 에러 방지를 위해 `proguard-rules.pro` 정밀 튜닝

**결과**
- 핵심 비즈니스 로직·보안 로직 역공학 원천 차단
- 난독화 + 코드 제거로 앱 바이너리 크기 **약 15~20% 감소**

---

###### ③ 하드웨어 보안 저장소 + Biometrics — Keychain / Keystore(TEE)

**문제**
기존 `AsyncStorage` 사용 시 데이터 평문 노출. 기기 분실·루팅 시 세션 토큰·개인정보 탈취 가능.

**해결**
- `AsyncStorage` 폐기 → iOS Keychain / Android Keystore(TEE) 기반 `react-native-keychain` 도입
- 보안 저장소 데이터 접근 시마다 OS 레벨 생체 인증(FaceID / TouchID / Fingerprint) 강제. `ACCESS_CONTROL.BIOMETRY_ANY` 옵션으로 Secure Enclave 하드웨어 키 해제 설계
- 생체 인식 일정 횟수 실패 시 민감 정보 즉시 파기(Self-destruct) → Fallback 우회 공격 차단

**결과**
- 기기 물리 탈취 시에도 데이터 복호화 불가 (Zero-Knowledge 방식에 근접)
- 금감원·금융보안원 '모바일 단말기 개인정보 암호화' 요구사항 충족

---

###### ④ OS 수준 화면 캡처·녹화 방지 — Anti-Screen Capture

**문제**
원격 제어 앱·스파이웨어를 통한 비밀번호·잔액 등 금융 정보 무단 캡처·녹화 위협.

**해결**
- **Android**: `WindowManager.LayoutParams.FLAG_SECURE` 적용 → 시스템 레벨에서 캡처·녹화·멀티태스킹 화면 노출 원천 차단
- **iOS**: 보안 필드 레이어를 활용해 화면 녹화 시 민감 정보 마스킹 처리

**결과**
- 시각적 데이터 탈취 시도 차단
- 금융 보안 가이드라인 화면 보호 요구사항 충족

---

##### 앱 성능 최적화 — 번들 분석 · 런타임 병목 탐지 · React 렌더링 개선

**배경**
`react-native-bundle-visualizer`(정적)와 `Flashlight + Maestro`(런타임) 두 도구를 병행하여 TTI 지연 및 런타임 CPU/RAM 병목을 정량적으로 측정·개선했습니다.

---

**① 정적 번들 분석 — react-native-bundle-visualizer**

Metro는 모듈 resolution을 Babel transform과 완전히 분리하는 구조로 `babel-plugin-module-resolver`·`extraNodeModules`로는 `@core/...` prefix alias 처리가 불가. `metro.config.js`에 `resolveRequest` 커스텀 함수를 추가해 분석 환경을 먼저 구성했습니다.

병목 분석 결과 (Total 10.59 MB, Mapped Rate 92%):

| 항목 | 점유율 | 내용 |
|---|---|---|
| `src/assets` | 30.6% (3.0 MB) | SVG 내부에 Base64 인코딩된 PNG 데이터 내장 |
| Victory 차트 계열 | 5.7% (~600 KB) | 특정 화면에서만 쓰이는 라이브러리가 초기 번들에 전량 포함 |
| `node-forge` | 2.8% (274 KB) | 미사용 Import로 인해 번들에 포함된 암호화 라이브러리 |

해결:
- **에셋 구조 개선**: SVG 내장 Base64 PNG → 독립 파일 분리, `mIcon.tsx` SVG/PNG 하이브리드 타입 분기 처리 → **2.0 MB 즉시 제거**
- **라이브러리 교체**: Victory 계열 → `react-native-gifted-charts` → **360 KB 제거**
- **Dead Code 제거**: 미사용 `forge` Import 삭제, 누적 중복 파일 13개 전수 조사 후 삭제

결과: JS Bundle Size **10.59 MB → 8.11 MB (▼ 2.48 MB, 23.4%)**

---

**② 런타임 병목 탐지 — Flashlight + Maestro**

Maestro 자동화 시나리오로 측정 오차를 제거하고 실제 기기 환경에서 CPU/RAM 병목 지점을 정량 식별했습니다.

해결:
- **탭 단위 Lazy Rendering**: 특정 탭 진입 시 CPU 300%+ 급등 원인 분석 → 5개 하위 컴포넌트가 동시 마운트되며 병렬 API 호출·렌더링 발생. 탭 단위 Lazy Rendering으로 전환하여 초기 JS 실행 부하 분산
- **ScrollView → FlatList 전환**: 화면에 보이지 않는 대량 아이템까지 일괄 마운트로 인한 **RAM 680 MB+ 과부하** 식별. FlatList 가상화로 비노출 메모리 로드 차단, `React.memo` + `useCallback` 결합 → **RAM 약 90 MB 절감**
- **useEffect 의존성 배열 개선**: 객체 참조 포함으로 인한 불필요한 API 재호출·리렌더링 반복 → 원시값 기반 추출로 수정
- **useMemo 적용**: 리스트 렌더링 시 복잡한 데이터 가공 로직 메모이제이션 → 렌더링 비용 최소화

결과:

| 지표 | 최적화 전 | 최적화 후 | 개선율 |
|---|---|---|---|
| 종합 성능 점수 | 71점 | 93점 | **▲ 31% 향상** |
| Average CPU usage | 106.2% | 92.7% | **▼ 13.5%p 개선** |
| High CPU Usage | 8s 지속 | None | **완전 해소** |
| Average RAM usage | 689.2 MB | 599.5 MB | **▼ 89.7 MB 절감** |
| Average Test Runtime | 37,500 ms | 16,500 ms | **▼ 56% 단축** |

---

## 기술 스택

| 분류 | 기술 |
|------|------|
| **핵심** | React Native, React, TypeScript, JavaScript |
| **Frontend** | HTML/CSS, TailwindCSS, Styled-components |
| **상태 관리** | React Query, Zustand, Jotai, Redux, Recoil, React Hook Form, Zod |
| **모바일** | Expo / EAS, Fastlane, SQLite |
| **Backend** | NestJS, Node.js, Express, Prisma |
| **API / 통신** | GraphQL, REST API, WebSocket, STOMP |
| **Database** | MySQL, PostgreSQL, MongoDB |
| **테스트** | Detox, Jest, Vitest |
| **도구** | Docker, Firebase, VSCode, Android Studio, Xcode, Claude, Cursor |

---

## 사이드 프로젝트

### 웹 보안 취약점 실습 프로젝트 `2026.03 – 진행 중`
의도적 취약 앱을 직접 설계·구현해 XSS·CSRF·SQL Injection 등 웹 공격 시나리오를 재현하는 보안 학습 프로젝트.
JWT/localStorage → Session → HttpOnly Cookie → Hybrid RT 4단계 인증 방식별 공격·방어 실습.
Next.js + NestJS + Docker 풀스택, 공격자 서버까지 직접 구성.

### 펫시터 매칭 서비스 Web & Server `2026.02 – 진행 중`
NestJS + Prisma + GraphQL 풀스택. 문서 주도 개발(API 명세 → 코드) 방식 적용.
Claude Subagents 활용으로 API 연동·에러 핸들링·컴포넌트 관심사 분리·디자인 시스템 체계화.

### 4:4 매칭 소셜앱 '핑퐁' `2024.10 – 2025.08`
4명씩 팀을 이뤄 매칭되는 소셜 앱. WebSocket 기반 실시간 매칭·채팅, 채팅 내 미니게임.
시간 기반 매칭 단계별 상태 머신 설계.

### AI 운동 상담 챗봇 '홈메이트' Web `2024.02 – 2024.03`
GPT API 연동 개인 맞춤형 운동 상담 챗봇. Service Worker 기반 Web Push 알림, PWA 구성.

### 대학교 중고거래 서비스 Web `2023.02 – 2023.09`
대학생 대상 캠퍼스 내 중고 거래 플랫폼. OAuth 소셜 로그인, 카카오 주소 검색 + 지오코딩 위치 기능.

### 멋쟁이사자처럼 10기 해커톤 3회 참여 `2022`
기획부터 개발까지 단기 해커톤 전 과정 참여. 팀 협업 및 빠른 프로토타이핑 경험.

---

## 학력

**한서대학교** 컴퓨터공학과 `2019.03 – 2025.02 졸업`
