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
```

## 사용법

1. 이 저장소를 클론합니다.
2. `claude --plugin-dir .` 로 플러그인을 로드합니다.
3. 등록된 스킬·에이전트·훅이 자동으로 활성화됩니다.

## 기여

스킬, 에이전트, 훅을 추가하려면 해당 디렉토리에 파일을 생성하고 `plugin.json`에 등록하세요.

## 라이선스

MIT
