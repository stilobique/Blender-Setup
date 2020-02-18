from win10toast import ToastNotifier
from os.path import join, dirname, abspath


def info_install(title, msg):
    """
    Simple function to show a Windows notification.
    :param title: Simple string texte, header information
    :param msg: long string whit a synthetic text
    """
    icon = join(dirname(abspath(__file__)), 'ressources', 'Blender.ico')
    toaster = ToastNotifier()
    toaster.show_toast(title=title,
                       msg=msg,
                       icon_path=icon,
                       duration=3)

