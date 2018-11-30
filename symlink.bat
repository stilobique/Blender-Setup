:: Make a loop with all folder to generate a sym link with blender
@echo off

:: Select your Blender version
set path_blender=%APPDATA%\Roaming\Blender Foundation\Blender
set /p version="Blender Version Used (2.xx) : " 
set subfolder=\scripts\addons

REM for /d %%d in (*.*) do (echo Cible %path_blender%\%%d Lien %CD%\%%d)
for /d %%d in (*.*) do (MKLINK /D "%path_blender%\%version%\%subfolder%\%%d" "%CD%\%%d")
