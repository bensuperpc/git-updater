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
import platform
import json


# Change to pull if you want merge local and remote
# Change to fetch if you want download repo from remote to local
# git push origin master #For local to remote without sync between
# git checkout -f HEAD


class git:
    major = "1"
    minor = "0"
    micro = "0"
    releaselevel = "final"

    def setgitproxy(self):
        os.system('git config --global --unset http.proxy')
        # os.system('git config --global http.proxy http://dominio\\vsilva:Passw0rd@195.53.86.82:3128')
        # os.system('git config --global http.proxy http://vsilva:Passw0rd@103.55.88.52:8080')
        os.system(
            "git config --global http.proxy http://dominio\vsilva:Passw0rd@103.55.88.52:8080")
        os.system('git config --global http.proxy')
        #  87.202.9.104:8080

    def gitupdate(self, maindirectory, thelist):

        print('maindirectory :' + maindirectory)

        print('thelist :', thelist)
        if platform.system() == 'Windows':
            print("SET PATH")
            os.system('SET PATH=%PATH%;C:\Program Files (x86)\Git\cmd;')

        # folder that contains repository
        # maindirectory = os.path.dirname(os.path.realpath(__file__))

        # Set current directory path to main folder
        os.chdir(maindirectory)

        # Repository URL list
        repositorylist = thelist

        for i in range(len(repositorylist)):
            # Repository URL
            repository = repositorylist[i]

            # get repository name ex : dolphin, vlc
            repositoryname = repository
            repositoryname = repositoryname.replace('.git', '')

            repositoryname = repositoryname.replace(
                repositoryname[:repositoryname.rindex('/') + 1], '')
            # Change current directory
            if platform.system() == 'Windows':
                # Current directory path of repository
                directory = maindirectory + '\\' + repositoryname
            else:
                # Current directory path of repository
                directory = maindirectory + '/' + repositoryname

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
                
				# Change default directory
                os.chdir(directory)

                print('Init :' + directory)
                os.system('git init ' + repository)
                print('Init OK')
                
                print('fetch :' + repository)
                os.system('git fetch --recurse-submodules -j2 -v ' + repository)
                print('fetch OK')
                
                
                os.system('git submodule update --init --recursive --remote')
                os.system('git submodule update --recursive --remote')
                print('Submodule : OK')

                #print('Check git integrity : ...')
                #os.system('git reflog expire --expire=now --all')
                #os.system('git gc --prune=now')
                #os.system('git fsck --full')
                #print('Check git integrity : OK')
                # os.system('git submodule update --recursive --remote')
                # 'git submodule update --init --recursive')
                # os.system('git submodule update --init --recursive ' + directory)

            else:
                # exists
                print("Folder exist")

                # Change default directory
                os.chdir(directory)

                # Test if git are init
                if os.system('git rev-parse --is-inside-work-tree') == 0:
                    # git are init
                    print('fetch :' + repository)
                    os.system('git fetch --recurse-submodules -j2 -v ' + repository)
                    print('fetch OK')
                    
                    #os.system('git reflog expire --expire=now --all')
                    #os.system('git gc --prune=now')
                    #os.system('git checkout -f .')
                    #os.system('git reset --hard')
                    #os.system('git fsck --full')
                    #print('checkout : OK')

                    print('Submodule...')
                    os.system(
                        'git submodule update --init --recursive --remote')
                    os.system('git submodule update --recursive --remote')
                    print('Submodule : OK')

                    # print('Check git integrity : ...')
                    # os.system('git reflog expire --expire=now --all')
                    # os.system('git gc --prune=now')
                    # os.system('git fsck --full')
                    # print('Check git integrity : OK')

                    # os.system('git branch')
                    # os.system('git tag')
                    # https://username:password@mygithost.com/my/repository
                else:
                    # git aren't init
                    print('Cloning :' + repository)
                    os.system('git clone -v ' + repository)
                    print("Cloning OK")

                    print('Init :' + directory)
                    os.system('git init ' + directory)

                    print('fetch :' + repository)
                    os.system('git fetch --recurse-submodules -j2 -v ' + repository)
                    print('fetch OK')

                    print('Submodule : ....')
                    os.system(
                        'git submodule update --init --recursive --remote')
                    os.system('git submodule update --recursive --remote')
                    print('Submodule : OK')

                    #print('Check git integrity : ...')
                    #os.system('git reflog expire --expire=now --all')
                    #os.system('git gc --prune=now')
                    #os.system('git fsck --full')
                    #print('Check git integrity : OK')
        print('==========================================')
        if platform.system() == 'Windows':
            # For Windows, change path
            os.system('SET PATH=%PATH%;c:\windows\system32;')

    def __init__(self):
        self.name = "gitclonepull"

    def class_version(self):
        return self.major + "." + self.minor + "." + self.micro + ":" + self.releaselevel


if __name__ == '__main__':
    objName = git()
    print("Lib Version : " + objName.class_version())
    repositorylist = ['https://github.com/dolphin-emu/dolphin.git',
                      # 'git://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/disco',
                      'https://github.com/Bensuperpc/Journal_lumineux.git',
                      'https://github.com/videolan/vlc.git',
                      'https://github.com/kornelski/7z.git',
                      'https://github.com/KDE/kdenlive.git',
                      'https://github.com/FFmpeg/FFmpeg.git',
                      'https://github.com/Microsoft/vscode.git',
                      'https://github.com/Microsoft/vscode-cpptools.git',
                      'https://github.com/HandBrake/HandBrake.git',
                      'https://github.com/snes9xgit/snes9x.git',
                      'https://github.com/torvalds/linux.git',
                      'https://github.com/Bensuperpc/DelayTime.git',
                      'https://github.com/darktable-org/darktable.git',
                      'https://github.com/kovidgoyal/calibre.git',
                      'https://github.com/KiCad/kicad-source-mirror.git',
                      'https://github.com/KiCad/kicad-symbols.git',
                      'https://github.com/KiCad/kicad-packages3D.git',
                      'https://github.com/FreeCAD/FreeCAD.git',
                      'https://github.com/FreeCAD/FreeCAD-addons.git',
					  'https://github.com/tensorflow/tensorflow.git',
					  'https://github.com/pmmp/PocketMine-MP.git',
					  'https://github.com/ShareX/ShareX.git',
                      'https://github.com/EpicGames/UnrealEngine.git', ]

    # Get current path of this script
    maindirectory = os.path.dirname(os.path.realpath(__file__))

    # objName.setgitproxy()
    objName.gitupdate(maindirectory, repositorylist)
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
# https://git-scm.com/book/en/v2/Git-Basics-Tagging


# SET PATH=%PATH%;C:\Program Files (x86)\Git\cmd;
# c:\windows\system32;
# ping wpad
# directory = 'G:\Logiciels et Scripts\DepotGit'
