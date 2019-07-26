:: Sym link about config file folder
@echo off

:: Test path before the symlink creation
set ConfigFolder=%blender_path%\%version%\config\

:: Generate all Symlink folder
set Repo=%CD%\blender-config


MKLINK /D "%ConfigFolder%" "%Repo%"

