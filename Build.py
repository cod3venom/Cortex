import os, shutil

chmod_allow_everything = 0o777
current_dir = os.getcwd()
build_dir = current_dir + '/build/'
cortex_config = '/usr/share/cortex'





if os.path.isdir(build_dir):
    os.chmod(build_dir, chmod_allow_everything)
    os.system(f'rm -rf {build_dir}')
    os.mkdir(build_dir)

else:
    os.mkdir(build_dir)
    os.chmod(build_dir, chmod_allow_everything)



shutil.copytree(cortex_config, build_dir + '/Cortex_config/')