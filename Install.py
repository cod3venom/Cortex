import os, sys

def pipinstall():
    with open('requirements.txt', 'r', encoding='utf8') as reader:
        lines = reader.read().split('\n')
        for line in lines:
            os.system(f'pip3 install {line}')


def installChrome():
    os.system(f'dpkg -i {os.getcwd()}/Core/Browser/Bin/google-chrome.deb')

if __name__ == "__main__":


    if sys.argv[1] == "install" and sys.argv[2] == "chrome":
        installChrome()
    if sys.argv[1] == "install" and sys.argv[2] == "pipinstall":
        pipinstall()

