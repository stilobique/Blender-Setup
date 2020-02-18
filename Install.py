from setup_notification import info_install

# Step Install Import
from setup_addons import addons_symlink
from setup_config import config_symlink

print('choose your blender version (2.xx) :')
bl_version = input()

# installation
if bl_version:
    print('Install config folder on blender {0}.'.format(bl_version))
    # addons
    install_addon = addons_symlink(bl_version)
    msg = '{0} addons has install.'.format(install_addon[1])
    info_install('B3D Addons Install', msg)
    print('All Addons has install.')

    # config
    install_config = config_symlink(bl_version)
    msg = 'The config folder has install'
    info_install('Blender Config', msg)

    # modules
    # preset

else:
    print('wrong number version.')

print('installation done. press a key to close this windows.')
