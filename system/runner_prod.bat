
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
set var6=%6
set var7=%7
set var8=%8
set var9=%9
set var10=%10
python -m utils.src  %var1% %var2% %var3% %var4% %var5% %var6% %var7% %var8% %var9% %var10%
REM &>>1 spinup.log


