
set ROOTPATH=C:\Users\CORBR\projects\corbisra
set PYTHONPATH=%ROOTPATH%;.
set HOME=%ROOTPATH%\utils
set ENVIRONMENT=DEV
echo %PYTHONPATH%
echo %HOME%

set var1=%1
set var2=%2
set var3=%3
set var4=%4
set var5=%5
python -m utils.src --Module %var1% --Class %var2% --Debug %var3%
REM &>>1 spinup.log


