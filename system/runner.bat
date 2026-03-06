
set PYTHONPATH=C:\scratch\svn\;.
set HOME=C:\scratch\svn\baseutils
echo %PYTHONPATH%

set var1=%1
set var2=%2
set var3=%3
set var4=%4
python -m baseutils.src --Module %var1% --Class %var2% --Debug %var3% 
REM &>>1 spinup.log


