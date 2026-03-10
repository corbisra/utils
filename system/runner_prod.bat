
set ROOTPATH=C:\Users\CORBR\projects\corbisra
set PYTHONPATH=%ROOTPATH%;.
set HOME=%ROOTPATH%\utils
set ENVIRONMENT=DEV
echo %PYTHONPATH%
echo %HOME%

set var1=%1
set var2=%2
shift
shift

set var3=%1
set var4=%2
shift
shift

set var5=%1
set var6=%2
shift
shift

set var7=%1
set var8=%2
shift
shift

set var9=%1
set var10=%2


python -m utils.src  %var1% %var2% %var3% %var4% %var5% %var6% %var7% %var8% %var9% %var10%
REM &>>1 spinup.log


