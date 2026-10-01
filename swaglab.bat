@echo off
call ".venv\Scripts\activate.bat"

pytest -v -s testClases\SwagLabE2E.py --browserName=edge

pause