
import os  # We need this module

# SET PATH=%PATH%;C:\Program Files (x86)\Git\cmd;
# c:\windows\system32;
# git config --global --unset http.proxy
# git config --global http.proxy http://dominio\vsilva:Passw0rd@195.53.86.82:3128

# git config --global http.proxy

# ping wpad
directory = 'C:\D\git\github'
repository = 'https://github.com/microsoft/Terminal.git'

os.system('SET PATH=%PATH%;C:\Program Files (x86)\Git\cmd;')

os.chdir(directory)
# os.system('git clone https://github.com/microsoft/Terminal.git')

# os.system('git init C:\D\git\github\Terminal')

if os.system('git rev-parse --is-inside-work-tree') == 0:
    print("Pulling :" + repository)
    os.system('git pull -v ' + repository)
    print("Pulling OK")
else:
    print("Cloning :" + repository)
    os.system('git clone -v ' + repository)
    print("Cloning OK")


os.system('SET PATH=%PATH%;c:\windows\system32;')

# cmd = "git --version"

# returned_value = os.system(cmd)  # returns the exit code in unix
# print('returned value:', returned_value)

# https://superuser.com/questions/1044961/commands-ping-and-ipconfig-are-not-recognized
# https://git-scm.com/docs/git-pull
# https://www.developpez.net/forums/d1143882/php/bibliotheques-frameworks/symfony/git-n-reconnu/
# https://blog.victorsilva.com.uy/failed-to-connect-to-github/
# https://www.seeyar.fr/liste-proxy/
