from os import getenv, listdir, makedirs, symlink
from os.path import abspath, dirname, join, isdir, isfile


def preset_symlink(bld_version):
    src_folder = join(dirname(abspath(__file__)), 'blender-presets')
    dst_folder = join(getenv('APPDATA'), 'Blender Foundation', 'Blender', bld_version, 'scripts', 'presets')
    try:
        config_folder = join(dst_folder, 'operator')
        if not isdir(dst_folder):
            makedirs(dst_folder)
        if not isdir(config_folder):
            symlink(src_folder, config_folder)
        return True
    except TypeError or FileNotFoundError or FileExistsError:
        return False
