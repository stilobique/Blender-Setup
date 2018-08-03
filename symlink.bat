:: Make a loop with all folder to generate a sym link with blender
@echo off

echo "Path like %APPDATA%\Roaming\Blender Foundation\Blender\2.XX\scripts\addons"
set /p path_blender="Blender Scripts folder : " 

REM for /d %%d in (*.*) do (echo Cible %path_blender%\%%d Lien %CD%\%%d)
for /d %%d in (*.*) do (MKLINK /D %path_blender%\%%d %CD%\%%d)

pause