from app.app_install import App_Install
from clientCCmd.ClientSSH import ClientSSH
import webbrowser

HOST = '127.0.0.1'

def __ask():

    ''' This function checks the answer of the user to continue the installation
    '''

    result = True
    answer = input('Enter your answer: ').lower()
    while (answer != 'yes' and answer != '' and answer != 'no'):
        answer = input('Enter a valid answer: ').lower()
    if (answer == 'no' ):
        result = False
    return result

def __step_by_step ():

    ''' This function perform step by step installation of the modules
    '''

    print (f"\n{'#'*10} Do you want to update the system? yes/no (YES)            {'#'*10}")
    UPDATE_SYSTEM = __ask()
    if (UPDATE_SYSTEM):
        ClientSSH.__run__(cmd, module.step1.update_system())
    
    print (f"\n{'#'*10} Do you want to install java? yes/no (YES)                 {'#'*10}")
    INSTALL_JAVA = __ask()
    if (INSTALL_JAVA):
        ClientSSH.__run__(cmd, module.step1.install_java())

    print (f"\n{'#'*10} Do you want to install the basic packages? yes/no (YES)   {'#'*10}")
    INSTALL_BASIC_PACKAGES = __ask()
    if (INSTALL_BASIC_PACKAGES):
        ClientSSH.__run__(cmd, module.step1.install_packages())

    print (f"\n{'#'*10} Do you want to install Wazuh Manager? yes/no (YES)        {'#'*10}")
    INSTALL_WAZUH_MANAGER = __ask()
    if (INSTALL_WAZUH_MANAGER):
        ClientSSH.__run__(cmd, module.step2.repo_wazuh())
        ClientSSH.__run__(cmd, module.step2.install_wazuh())
        ClientSSH.__run__(cmd, module.step2.install_elasticsearch())
        ClientSSH.__run__(cmd, module.step2.install_filebeat())
        ClientSSH.__run__(cmd, module.step2.install_kibana())

    print (f"\n{'#'*10} Do you want to configure the firewall? yes/no (YES)     {'#'*10}")
    CONFIG_FIREWALL = __ask()
    if (CONFIG_FIREWALL):
        ClientSSH.__run__(cmd, module.step2.config_firewall())

def __unattended():

    ''' This function perform unattended installation of the modules
    '''

    ClientSSH.__run__(cmd, module.step1.update_system())
    ClientSSH.__run__(cmd, module.step1.install_java())
    ClientSSH.__run__(cmd, module.step1.install_packages())
    ClientSSH.__run__(cmd, module.step2.repo_wazuh())
    ClientSSH.__run__(cmd, module.step2.install_wazuh())
    ClientSSH.__run__(cmd, module.step2.install_elasticsearch())
    ClientSSH.__run__(cmd, module.step2.install_filebeat())
    ClientSSH.__run__(cmd, module.step2.install_kibana())
    ClientSSH.__run__(cmd, module.step2.config_firewall())


if __name__ == '__main__':
   
    print (f"\n{'#'*10}                 Welcome to Wazuh Installer                 {'#'*10}")
    print (f"\n{'#'*10} Firstly, you must choose which modules you want to install {'#'*10}")
    print (f"\n{'#'*10}    After that, the installation process will guide you     {'#'*10}")
    print (f"\n{'#'*10}                 through the different steps                {'#'*10}\n")

    print (f"\n{'#'*10} What is the IP of the server where you want deploy Wazuh?  {'#'*10}")
    HOST = input("Enter the IP: ")
    while True:
        result = input ("Is the IP %s correct? yes/no (YES): " %{HOST}).lower()
        if (result == 'yes' or result == ''):
            break
        elif (result == 'no'):
            HOST = input("Enter the correct IP: ")
        else:
            print ('Enter a valid answer')

    print (f"\n{'#'*10}   The SSH connection to the server will be established    {'#'*10}")
    print (f"\n{'#'*10}  Enter Username and Password to complete the connection   {'#'*10}\n")

    client, cmd = ClientSSH.__clientSSH__(HOST)
    module = App_Install()

    print (f"\n{'#'*10}   Do you want Step by Step or Unattended installation?     {'#'*10}\n")
    option = input("Write (1) for a Step by Step installation or write (2) for unattended installation: ")
    while True:
        if option == '1':
            __step_by_step()
            break
        elif option == '2':
            __unattended()
            break
        else:
            print (f"\n{'#'*10}            You must write a valid answer.                 {'#'*10}")
            option = input("Write (1) for a Step by Step installation or write (2) for unattended installation: ")
    
    ClientSSH.__clientSSHclose__(client)

    print (f"\n{'#'*10}           Everything was installed successfully          {'#'*10}")
    print (f"\n{'#'*10}                           ENJOY                           {'#'*10}\n")

    webbrowser.open_new('https://documentation.wazuh.com/4.2/getting-started/')
    webbrowser.open_new('https://'+HOST)
    