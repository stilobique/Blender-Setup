@echo off
:: Generate Data
set blender_path=%APPDATA%\Blender Foundation\Blender
set /p version="Blender Version Used (2.xx) : " 

:: Install Addons
:: Generate Symlink
call install_addons.bat %version% %blender_path%

:: Install GoB
call install_GoB.bat

:: Install Preset
call install_preset.bat %version% %blender_path%

:: Install Modules
call install_modules.bat %version% %blender_path%

pause