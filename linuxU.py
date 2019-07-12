import os


def update(your_os):
    if your_os == 'Debian' or your_os == 'debian' or your_os == 'Ubuntu' or your_os == 'ubuntu':
        print('Update Starts')
        os.system('sudo apt update')
    elif your_os == 'Fedora' or your_os == 'fedora' or your_os == 'Centos' or your_os == 'centos':
        print('Update Starts')
        os.system('sudo yum update')


def upgrade(your_os):
    if your_os == 'Debian' or your_os == 'debian' or your_os == 'Ubuntu' or your_os == 'ubuntu':
        print('Upgrade Starts')
        os.system('sudo apt upgrade')
    elif your_os == 'Fedora' or your_os == 'fedora' or your_os == 'Centos' or your_os == 'centos':
        print('Upgrade Starts')
        os.system('sudo yum upgrade')


def autoremove(your_os):
    if your_os == 'Debian' or your_os == 'debian' or your_os == 'Ubuntu' or your_os == 'ubuntu':
        print('Autoremove Starts')
        os.system('sudo apt autoremove')
    elif your_os == 'Fedora' or your_os == 'fedora' or your_os == 'Centos' or your_os == 'centos':
        print('Autoremove Starts')
        os.system('sudo yum autoremove')