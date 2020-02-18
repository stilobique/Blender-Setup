from os import getenv, listdir, makedirs, symlink
from os.path import abspath, dirname, join, isdir, isfile


def addons_symlink(bld_version):
    src_folder = join(dirname(abspath(__file__)), 'blender-addons')
    dst_folder = join(getenv('APPDATA'), 'Blender Foundation', 'Blender', bld_version, 'scripts', 'addons')
    try:
        if not isdir(dst_folder):
            makedirs(dst_folder)
        for addon in listdir(src_folder):
            link_src = join(src_folder, addon)
            dst_src = join(dst_folder, addon)
            if not isdir(dst_src) and not isfile(dst_src):
                symlink(link_src, dst_src)
        count_addons = len(listdir(src_folder))
        return True, count_addons
    except TypeError or FileNotFoundError:
        return False
