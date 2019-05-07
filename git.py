#
#
# git.py - for git clone and pull in local
#
# Created by Benoît(Bensuperpc@gmail.com) 07th may 2019
# Updated by X for python 3.X
#
# Released into the Public domain with MIT licence
# https://opensource.org/licenses/MIT
#
# Written with Sublime text 3 and python 3.7.3
# Script compatibility : Windows, soon Linux
# Script requirement : python 3.4 and above, git 2.X
#
# ==============================================================================

import os  # We need this module
import os.path
from pathlib import Path
import sys


class gitpull:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"

    def gitpull(self, maindirectory, thelist):
        # For Windows, change path
        # print(self)
        print('maindirectory :' + maindirectory)

        print('thelist :', thelist)

        os.system('SET PATH=%PATH%;C:\Program Files (x86)\Git\cmd;')

        # folder that contains repository
        # maindirectory = os.path.dirname(os.path.realpath(__file__))

        # Set current directory path to main folder
        os.chdir(maindirectory)

        # Repository URL list
        repositorylist = thelist

        for i in range(len(repositorylist)):
            # Repository URL
            # 'https://github.com/microsoft/Terminal.git'
            repository = repositorylist[i]

            # get repository name ex : dolphin, vlc
            repositoryname = repository
            repositoryname = repositoryname.replace('.git', '')
            repositoryname = repositoryname.replace(
                repositoryname[:repositoryname.rindex('/') + 1], '')

            # Current directory path of repository
            directory = maindirectory + '\\' + repositoryname

            # Check if current directory path of repository exist
            my_file = Path(directory)
            print('directory :' + directory)
            try:
                my_abs_path = my_file.resolve(strict=True)
                del my_abs_path
            except FileNotFoundError:
                # doesn't exist
                print("Folder not exist")

                # Change default directory
                os.chdir(maindirectory)

                print("Cloning :" + repository)
                os.system('git clone -v ' + repository)
                print("Cloning OK")

                print('Init :' + directory)
                os.system('git init ' + directory)

            else:
                # exists
                print("Folder exist")

                # Change default directory
                os.chdir(directory)

                if os.system('git rev-parse --is-inside-work-tree') == 0:
                    print('Pulling :' + repository)
                    os.system('git pull -v ' + repository)
                    print('Pulling OK')
                else:
                    # os.system('git init C:\D\git\github\Terminal')
                    print('Cloning :' + repository)
                    os.system('git clone -v ' + repository)
                    print("Cloning OK")
                    # os.system('git init C:\D\git\github\Terminal')
                    os.system('git init ' + directory)

        # For Windows, change path
        os.system('SET PATH=%PATH%;c:\windows\system32;')

    def __init__(self):
        self.name = "gitclonepull"

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel


if __name__ == '__main__':
    objName = gitpull()
    print("Lib Version : " + objName.class_version())
    repositorylist = ['https://github.com/dolphin-emu/dolphin.git',
                      'https://github.com/Bensuperpc/Journal_lumineux.git',
                      'https://github.com/videolan/vlc.git',
                      'https://github.com/kornelski/7z.git',
                      'https://github.com/HandBrake/HandBrake.git']

    # objName.gitpull(repositorylist)
    maindirectory = os.path.dirname(os.path.realpath(__file__))
    objName.gitpull(maindirectory, repositorylist)

    # count the arguments
    arguments = len(sys.argv) - 1
    position = 1
    while (arguments >= position):
        print("parameter %i: %s" % (position, sys.argv[position]))
        position = position + 1

    # objName.install_KDE()


# cmd = "git --version"

# returned_value = os.system(cmd)  # returns the exit code in unix
# print('returned value:', returned_value)

# https://superuser.com/questions/1044961/commands-ping-and-ipconfig-are-not-recognized
# https://git-scm.com/docs/git-pull
# https://www.developpez.net/forums/d1143882/php/bibliotheques-frameworks/symfony/git-n-reconnu/
# https://blog.victorsilva.com.uy/failed-to-connect-to-github/
# https://www.seeyar.fr/liste-proxy/
# https://stackoverflow.com/questions/9572490/find-index-of-last-occurrence-of-a-substring-in-a-string
# https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions?page=1&tab=oldest#tab-top
# https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
# https://stackoverflow.com/questions/32554527/typeerror-list-indices-must-be-integers-or-slices-not-str

# SET PATH=%PATH%;C:\Program Files (x86)\Git\cmd;
# c:\windows\system32;
# git config --global --unset http.proxy
# git config --global http.proxy http://dominio\vsilva:Passw0rd@195.53.86.82:3128
# git config --global http.proxy
# ping wpad
# directory = 'G:\Logiciels et Scripts\DepotGit'
