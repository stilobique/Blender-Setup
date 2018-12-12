:: Make a loop with all folder to generate a sym link with blender
@echo off
cd blender-addons

:: Test path before the symlink creation
set TestFolder1=%blender_path%\%version%\scripts\
if not exist "%TestFolder1%" mkdir "%TestFolder1%"

set TestFolder2=%TestFolder1%\addons\
if not exist "%TestFolder2%" mkdir "%TestFolder2%"

:: Generate all Symlink folder
set subfolder=scripts\addons
for /d %%d in (*.*) do (MKLINK /D "%blender_path%\%version%\%subfolder%\%%d" "%CD%\%%d")

cd ..
