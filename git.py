#
#
# git.py - for git clone and pull in local
#
# Created by Benoît(Bensuperpc@gmail.com) 07th may 2019
# Updated by Benoît(Bensuperpc@gmail.com) 17 th March 2020
# 
#
# Released into the Public domain with MIT licence
# https://opensource.org/licenses/MIT
#
# Written with Sublime text 3 and python 3.7.3
# Updated with Visual Studio code 1.42.1 and python 3.8.2
# Script compatibility : Windows, Linux, Mac
# Script requirement : python 3.5 and above, git 2.2X
#
# ==============================================================================

import os  # We need this module
import subprocess

def get_repo_name(repo_url):
    repo_url = repo_url.replace('.git', '')
    repo_url = repo_url.replace(repo_url[:repo_url.rindex('/') + 1], '')
    return repo_url


def git_update(repos_directory, list_of_repos):
    print('maindirectory :' + repos_directory)
    print('thelist :', list_of_repos)

    for repos in list_of_repos:
        file_name = get_repo_name(repos)
        #os.system('git fsck --full')
        if os.path.exists(file_name):
            print('exist')
            subprocess.run(
                ['git', '-C', file_name + '/', 'pull', '--all', '--recurse-submodules', '-j2'])
            subprocess.run(
                ['git', '-C', file_name + '/', 'submodule', 'update', '--recursive', '--remote'])
        else:
            print("Cloning :" + repos)
            subprocess.run(
                ['git', 'clone', '-v', repos, '--recurse-submodules', '-j2'])
            subprocess.run(
                ['git', '-C', file_name + '/', 'pull', '--all'])
            print("Cloning OK")


if __name__ == '__main__':
    with open('repos.txt') as f:
        repositorylist = f.readlines()
    repositorylist = [x.strip() for x in repositorylist]

    # Get current path of this script
    maindirectory = os.path.dirname(os.path.realpath(__file__))
    git_update(maindirectory, repositorylist)
