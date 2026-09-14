<#
  write-black-titan-serial 스킬 정본 → 설치본 동기화

  정본 : 08_CODEX_이관\write-black-titan-serial\   (Drive 이관 원본. 여기만 편집한다)
  설치본: .claude\skills\write-black-titan-serial\  (파생본. 매번 통째로 덮어쓴다)

  사용:  pwsh -File sync-skill.ps1
         pwsh -File sync-skill.ps1 -Check    # 차이만 확인하고 덮어쓰지 않음
#>
param([switch]$Check)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$src  = Join-Path $root '08_CODEX_이관\write-black-titan-serial'
$dst  = Join-Path $root '.claude\skills\write-black-titan-serial'

if (-not (Test-Path $src)) { throw "정본이 없다: $src" }

function Get-Manifest($base) {
    if (-not (Test-Path $base)) { return @{} }
    $m = @{}
    Get-ChildItem -Recurse -File $base | ForEach-Object {
        $rel = $_.FullName.Substring($base.Length).TrimStart('\')
        $m[$rel] = (Get-FileHash $_.FullName -Algorithm SHA256).Hash
    }
    return $m
}

$a = Get-Manifest $src
$b = Get-Manifest $dst

$added   = $a.Keys | Where-Object { -not $b.ContainsKey($_) }
$removed = $b.Keys | Where-Object { -not $a.ContainsKey($_) }
$changed = $a.Keys | Where-Object { $b.ContainsKey($_) -and $a[$_] -ne $b[$_] }

if (-not ($added -or $removed -or $changed)) {
    Write-Host "동일함 — 정본과 설치본이 일치한다 ($($a.Count)개 파일)."
    return
}

foreach ($f in $added)   { Write-Host "  + $f" }
foreach ($f in $changed) { Write-Host "  ~ $f" }
foreach ($f in $removed) { Write-Host "  - $f  (설치본에만 존재. 덮어쓰면 사라진다)" }

if ($Check) { Write-Host "`n-Check 모드라 덮어쓰지 않았다."; return }

if (Test-Path $dst) { Remove-Item -Recurse -Force $dst }
New-Item -ItemType Directory -Force (Split-Path $dst) | Out-Null
Copy-Item -Recurse -Force $src $dst

$n = (Get-ChildItem -Recurse -File $dst).Count
Write-Host "`n동기화 완료 — $n개 파일. 새 세션부터 반영된다."
