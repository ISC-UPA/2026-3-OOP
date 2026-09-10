@echo off
cls
git pull
git status
timeout /t 2

for /f %%i in ('wmic os get localdatetime ^| find "."') do set datetime=%%i
set FECHA=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2% %datetime:~8,2%:%datetime:~10,2%

git add .
git commit -m "Auto %FECHA%"
git push

pause
cls







