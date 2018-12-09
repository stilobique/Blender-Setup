:: Make a loop with all folder to generate a sym link with blender
@echo off
cd blender-addons

:: Select your Blender version
set path_blender=%APPDATA%\Blender Foundation\Blender
set /p version="Blender Version Used (2.xx) : " 

:: Test path before the symlink creation
set TestFolder1=%path_blender%\%version%\scripts\
if not exist "%TestFolder1%" mkdir "%TestFolder1%"

set TestFolder2=%TestFolder1%\addons\
if not exist "%TestFolder2%" mkdir "%TestFolder2%"

:: Generate all Symlink folder
set subfolder=scripts\addons
for /d %%d in (*.*) do (echo Cible %path_blender%\%%d Lien %CD%\%%d)
for /d %%d in (*.*) do (MKLINK /D "%path_blender%\%version%\%subfolder%\%%d" "%CD%\%%d")

cd ..
