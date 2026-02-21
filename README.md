# claude-alchemy

클로드 코드를 극한으로 활용하기 위한 스킬·에이전트·훅 모음 플러그인.

## 설치

```bash
# 로컬에서 바로 사용
claude --plugin-dir /path/to/claude-alchemy

# 또는 프로젝트 루트에서
claude --plugin-dir .
```

## 구조

```
.claude-plugin/
├── plugin.json          ← 플러그인 매니페스트
└── marketplace.json     ← 마켓플레이스 정의
skills/                  ← 스킬 모음
agents/                  ← 에이전트 모음
hooks/                   ← 훅 모음
plugins/                 ← 플러그인 모음
  statusline-usage/      ← 구독 사용량 스테이터스라인
```

## 플러그인

### statusline-usage

구독 사용량을 실시간 표시하는 스테이터스라인.

```
Opus 4.6 | main* | 20k/200k | 5h 18% (2h34m) | 7d 32% (3d20h)
```

- macOS 키체인에서 OAuth 토큰 읽기 → Anthropic Usage API 호출
- 외부 의존성 없음 (Python stdlib only)
- `/setup-statusline` 명령어로 설치

## 사용법

1. 이 저장소를 클론합니다.
2. `claude --plugin-dir .` 로 플러그인을 로드합니다.
3. 등록된 스킬·에이전트·훅이 자동으로 활성화됩니다.

## 기여

스킬, 에이전트, 훅을 추가하려면 해당 디렉토리에 파일을 생성하고 `plugin.json`에 등록하세요.

## 라이선스

MIT
