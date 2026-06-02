@echo off
mode con: cols=68 lines=14
cd /d "%~dp0"
where python >nul 2>nul
if %errorlevel%==0 (
    python "%~dp0serve.py" %*
    goto :end
)
where py >nul 2>nul
if %errorlevel%==0 (
    py "%~dp0serve.py" %*
    goto :end
)
where python3 >nul 2>nul
if %errorlevel%==0 (
    python3 "%~dp0serve.py" %*
    goto :end
)
echo Python nao encontrado. Instale Python 3 em https://python.org
pause
:end
