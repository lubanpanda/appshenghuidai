import os
from os import walk


def installAllApks(dir='./'):
    for (dirpath, dirnames, filenames) in walk(dir):
        for file in filenames:
            if file.endswith('.apk'):
                installApk(file)


def installApk(file):
    if os.system("adb install " + file) != 0:
        exit('error')
        print('instatll ' + file + ' success')


if __name__ == '__main__':
    installAllApks()
