
set PYTHONPATH=C:\scratch\svn\;.
set HOME=C:\scratch\svn\baseutils
set ENVIRONMENT=C:\scratch\svn\baseutils
set ENVIRONMENT=DEV
echo %PYTHONPATH%

set var1=%1
set var2=%2
set var3=%3
set var4=%4
set var5=%5
python -m baseutils.src --Module %var1% --Class %var2% --Debug %var3% --BuildRunbook %var4% --ValueDate 
REM &>>1 spinup.log


