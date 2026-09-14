@echo off
chcp 65001 >nul
cd /d "%~dp0"
netstat -ano | findstr /r /c:":8787 .*LISTENING" >nul
if errorlevel 1 (
  echo review server starting on port 8787...
  start "review-server-8787" cmd /k python tools\review_server.py
  timeout /t 2 /nobreak >nul
) else (
  echo review server already running on 8787.
)
start http://localhost:8787
