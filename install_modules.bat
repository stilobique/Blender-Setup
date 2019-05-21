:: Make a loop with all folder to generate a sym link with blender
@echo off
cd blender-modules

:: Test path before the symlink creation
set subfolder=scripts\modules
set Modules_Folder=%blender_path%\%version%\%subfolder%\
if not exist "%Modules_Folder%" mkdir "%Modules_Folder%"

:: Generate all Symlink folder
for /d %%d in (*.*) do (MKLINK /D "%blender_path%\%version%\%subfolder%\%%d" "%CD%\%%d")

cd ..
