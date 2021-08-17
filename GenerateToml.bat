@echo off

git pull

python --version 3>NUL

if not errorlevel 0 GOTO :NOPYTHON

cd toml

python GenerateToml.py --print %1

pause

:NOPYTHON
echo.
echo Error^: Python not installed