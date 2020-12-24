import os, sys
import shutil


def pipinstall():
    with open('requirements.txt', 'r', encoding='utf8') as reader:
        lines = reader.read().split('\n')
        for line in lines:
            os.system(f'pip3 install {line}')


def installChrome():
    os.system(f'dpkg -i {os.getcwd()}/Core/Browser/Bin/google-chrome.deb')

def installConfig():
    os.system('cp -r build/Cortex_config/* /usr/share/cortex')

if __name__ == "__main__":


    if sys.argv[1] == "install" and sys.argv[2] == "chrome":
        installChrome()
    if sys.argv[1] == "install" and sys.argv[2] == "pipinstall":
        pipinstall()

    if sys.argv[1] == "install" and sys.argv[2] == "config":
        installConfig()

