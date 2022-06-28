#from getpass import getpass, getuser
#from platform import python_branch
from app.app_install import App_Install
from clientCCmd.ClientSSH import ClientSSH
from settings import *

## def progress_bar (progress, total, color=colorama.Fore.YELLOW):
##     percent = 100 * (progress / float(total))
##     bar = '#' * int(percent) + '-' * (100 - int(percent))
##     print (color +  f"\r|{bar}| {percent:.2f}%", end="\r")
##     if progress == total:
##         print (colorama.Fore.GREEN +  f"\r|{bar}| {percent:.2f}%", end="\r")

## numbers = [x * 5 for x in range (2000, 3000)]
## results = []
## 
## progress_bar(0, len(numbers))
## for i, x in enumerate(numbers):
##     results.append(math.factorial(x))
##     progress_bar(i + 1, len(numbers))

if __name__ == '__main__':

#    HOST='192.168.78.65'
#    HOST='192.168.1.140'
   
    client, cmd = ClientSSH.__clientSSH__(HOST)
   
    module = App_Install()
#    print (module.step1.update)

#    ClientSSH.__run__(cmd, module.test_command())

    ClientSSH.__run__(cmd, module.step1.update_system())
    ClientSSH.__run__(cmd, module.step1.install_java())
    ClientSSH.__run__(cmd, module.step1.install_packages())

    ClientSSH.__run__(cmd, module.step2.install_wazuh())
    ClientSSH.__run__(cmd, module.step2.install_elasticsearch())
    ClientSSH.__run__(cmd, module.step2.install_filebeat())
    ClientSSH.__run__(cmd, module.step2.install_kibana())
    ClientSSH.__run__(cmd, module.step2.config_firewall())

    ClientSSH.__clientSSHclose__(client)