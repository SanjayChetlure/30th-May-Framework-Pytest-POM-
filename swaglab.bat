@echo off
call ".venv\Scripts\activate.bat"
pytest -v -s testClases\SwagLabLogin_WithFixture4.py --browser=chrome -n 2 --html=Reports\SwaglabREport.html
pause