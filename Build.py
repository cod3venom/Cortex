import os

current_dir = os.getcwd()
build_dir = current_dir + '/build'
cortex_config = '/usr/share/cortex'


if os.path.isdir(build_dir):
    for root, dirs, files in os.walk(build_dir, topdown=False):
        for name in files:
            os.remove(os.path.joint(root,name))
        for dir in dirs:
            os.rmdir(os.path.join(dir))