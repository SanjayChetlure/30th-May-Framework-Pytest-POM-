@echo off
call ".venv\Scripts\activate.bat"

pytest -v -s testClases\SwagLabLogin_WithFixture5.py -m "smoke or regression" --browserName=chrome

pause