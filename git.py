
import os  # We need this module
import os.path
from pathlib import Path

# For Windows, change path
os.system('SET PATH=%PATH%;C:\Program Files (x86)\Git\cmd;')

# folder that contains files
maindirectory = 'C:\D\git\github'
os.chdir(maindirectory)

repositorylist = ['https://github.com/dolphin-emu/dolphin.git',
                  'https://github.com/Bensuperpc/Journal_lumineux.git',
                  'https://github.com/HandBrake/HandBrake.git']
# .
# .


repository = 'https://github.com/microsoft/Terminal.git'
repositoryname = 'https://github.com/microsoft/Terminal.git'
repositoryname = repositoryname.replace('.git', '')
repositoryname = repositoryname.replace(
    repositoryname[:repositoryname.rindex('/') + 1], '')

directory = maindirectory + '\\' + repositoryname

my_file = Path(directory)
try:
    my_abs_path = my_file.resolve(strict=True)
except FileNotFoundError:
    # doesn't exist
    print("Not exist")
    print("Cloning :" + repository)
    os.system('git clone -v ' + repository)
    print("Cloning OK")

    os.system('git init ' + directory)

else:
    # exists
    print("Exist")
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


# os.system('git clone https://github.com/microsoft/Terminal.git')
# os.system('git show-ref refs/heads/Terminal')
# os.system('git rev-parse --verify Terminal')

# for w in words:


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

# SET PATH=%PATH%;C:\Program Files (x86)\Git\cmd;
# c:\windows\system32;
# git config --global --unset http.proxy
# git config --global http.proxy http://dominio\vsilva:Passw0rd@195.53.86.82:3128
# git config --global http.proxy
# ping wpad
# directory = 'G:\Logiciels et Scripts\DepotGit'
