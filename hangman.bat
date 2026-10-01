@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>&1
if not errorlevel 1 (
    py -3 "%~dp0hangman.py"
) else (
    python "%~dp0hangman.py"
)

if errorlevel 1 pause