:: Install file for Zbrush
@echo off
echo "Install GoZ on Zbrush"
set path_zbrush=C:\Users\Public\Pixologic\GoZApps\Blender

xcopy /E GoB\Blender %path_zbrush%
