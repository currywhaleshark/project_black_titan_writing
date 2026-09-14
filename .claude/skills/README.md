# 이 폴더는 파생본이다

`write-black-titan-serial/`은 정본의 사본이며, 동기화할 때마다 **통째로 지워지고 다시 복사된다.**
여기서 고친 내용은 다음 동기화에서 사라진다.

- 정본: `08_CODEX_이관/write-black-titan-serial/` — 스킬 수정은 여기서만 한다
- 동기화: 프로젝트 루트에서 `pwsh -File sync-skill.ps1`
- 차이 확인만: `pwsh -File sync-skill.ps1 -Check`

스킬 목록은 세션 시작 시 로드되므로, 동기화 후에는 세션을 새로 열어야 반영된다.
