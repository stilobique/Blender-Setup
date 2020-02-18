from setup_notification import info_install

# Step Install Import
from setup_addons import addons_symlink
from setup_config import config_symlink
from setup_modules import modules_symlink
from setup_preset import preset_symlink

print('choose your blender version (2.xx) :')
bl_version = input()

try:
    float(bl_version)
    print('Install config folder on blender {0}.'.format(bl_version))
    # addons
    install_addon = addons_symlink(bl_version)
    msg = '{0} addons has install.'.format(install_addon[1])
    info_install('B3D Addons Install', msg)
    print(msg)

    # config
    install_config = config_symlink(bl_version)
    msg = 'The config folder has install'
    info_install('Blender Config', msg)
    print(msg)

    # modules
    install_module = modules_symlink(bl_version)
    msg = 'All modules has added'
    info_install('Blender Modules', msg)
    print(msg)

    # preset
    install_preset = preset_symlink(bl_version)
    msg = 'All preset has added'
    info_install('Blender Preset', msg)
    print(msg)
    msg = 'All setup for Blender {0} has install.'.format(bl_version)

except ValueError:
    msg = 'Wrong number version.'

info_install('Blender Setup', msg)
print(msg)
