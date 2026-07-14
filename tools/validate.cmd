@echo off
setlocal

set ROOT=%~dp0..

cd /d "%ROOT%"

py tools\validate_project.py %*

endlocal