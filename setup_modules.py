from os import getenv, listdir, makedirs, symlink
from os.path import abspath, dirname, join, isdir, isfile


def modules_symlink(bld_version):
    src_folder = join(dirname(abspath(__file__)), 'blender-modules')
    dst_folder = join(getenv('APPDATA'), 'Blender Foundation', 'Blender', bld_version, 'scripts', 'modules')
    try:
        if not isdir(dst_folder):
            makedirs(dst_folder)
        for module in listdir(src_folder):
            link_src = join(src_folder, module)
            dst_src = join(dst_folder, module)
            if not isdir(dst_src) and not isfile(dst_src):
                symlink(link_src, dst_src)
        count_addons = len(listdir(src_folder))
        return True, count_addons
    except TypeError or FileNotFoundError:
        return False
