from os import getenv, listdir, makedirs, symlink
from os.path import abspath, dirname, join, isdir, isfile


def config_symlink(bld_version):
    src_folder = join(dirname(abspath(__file__)), 'blender-config')
    dst_folder = join(getenv('APPDATA'), 'Blender Foundation', 'Blender', bld_version)
    try:
        if not isdir(dst_folder):
            makedirs(dst_folder)
        symlink(src_folder, join(dst_folder, 'config'))
        return True
    except TypeError or FileNotFoundError:
        return False
