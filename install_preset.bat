:: Make a loop with all folder to generate a sym link with blender
REM @echo off
cd blender-presets

echo Test show version : %version%
:: Test path before the symlink creation
set TestFolder1=%blender_path%\%version%\scripts\
if not exist "%TestFolder1%" mkdir "%TestFolder1%"

set TestFolder2=%TestFolder1%\presets\operator
if not exist "%TestFolder2%" mkdir "%TestFolder2%"

:: Generate all Symlink folder
set subfolder=scripts\presets\operator
for /d %%d in (*.*) do (
	if %%d neq .idea (
	MKLINK /D "%blender_path%\%version%\%subfolder%\%%d" "%CD%\%%d"
	)
)

cd ..
