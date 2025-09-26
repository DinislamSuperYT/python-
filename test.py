class Linux():
    version = 6
    name = "Linux"
    author = "Linus Torvalds"

class Distro(Linux):
    distro_ver = None
    de = None
    author = None
    Karnel_ver = None
    boot = None
    init = None
    pack_manager = None
    GPU = None
    CPU = None
    root = True

class Ubuntu(Linux, Distro):
    de = 'GNOME'
    author = 'Ubuntu Community'
    distro_ver = 25
    Karnel_ver = version
    boot = 'GRUB'
    init = 'systemd'
    pack_manager = ['apt', 'dpkg', 'flatpack']
    GPU = ['NVidia', 'AMD', 'Intel']
    CPU = ('x86_64', 'x86_32', 'arm_64', 'arm_32')
    root = True

class AUSP(Linux, Distro):
    distro_ver = 15
    author = 'Google'
    de = 'AUSP_DE_CUSTOM'
    Karnel_ver = version
    boot = "Android_boot"
    init = 'Android_init'
    CPU = ('arm_64')
    root = False