# claude-alchemy

클로드 코드를 극한으로 활용하기 위한 스킬·에이전트·훅·플러그인 모음.

## 저장소

- GitHub: https://github.com/craftowen/claude-alchemy
- 변경사항은 반드시 이 저장소에 커밋/푸시한다.

## 프로젝트 구조

```
skills/          ← 스킬 모음
agents/          ← 에이전트 모음
hooks/           ← 훅 모음
plugins/         ← 플러그인 모음
  statusline-usage/  ← 구독 사용량 스테이터스라인
```

## 플러그인 개발 규칙

- 새 플러그인/스킬/에이전트/훅을 만들면 이 저장소(`plugins/`, `skills/`, `agents/`, `hooks/`)에 추가한다.
- 로컬 전용 경로(`~/.claude/plugins/marketplaces/...`)가 아닌 이 저장소에 원본을 둔다.
- 작업 완료 후 커밋/푸시까지 진행한다.

## 마켓플레이스 스키마 (중요)

`.claude-plugin/marketplace.json`은 반드시 공식 스키마를 따라야 한다.
새 플러그인 추가 시 `plugins` 배열에 항목을 추가할 것.

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "claude-alchemy",
  "description": "...",
  "owner": { "name": "owen", "email": "" },
  "plugins": [
    {
      "name": "플러그인명",
      "description": "설명",
      "version": "1.0.0",
      "author": { "name": "owen", "email": "" },
      "source": "./plugins/플러그인명",
      "category": "productivity"
    }
  ]
}
```

필수 필드: `name`, `owner` (object), `plugins` (array).
`slug`, `displayName`, `tagline` 등은 무시됨 — 공식 스키마와 다르면 설치 실패한다.
