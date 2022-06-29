from app.app_install import App_Install
from clientCCmd.ClientSSH import ClientSSH
import webbrowser

HOST = '127.0.0.1'

def ask():
    result = True
    answer = input('Enter your answer: ').lower()
    while (answer != 'yes' and answer != '' and answer != 'no'):
        answer = input('Enter a valid answer: ').lower()
    if (answer == 'no' ):
        result = False
    return result
        

if __name__ == '__main__':
   
    print (f"\n{'#'*10}                 Welcome to Installer Wazuh                {'#'*10}\n")
    print (f"\n{'#'*10} Firstly, you must choice which modules yo want to install {'#'*10}\n")
    print (f"\n{'#'*10}    After that, the installation process will guide you    {'#'*10}\n")
    print (f"\n{'#'*10}                 through the different steps               {'#'*10}\n")

    print (f"\n{'#'*10} What is the IP of the server where you want deploy Wazuh? {'#'*10}\n")
    HOST = input("Enter the IP: ")
    while True:
        result = input ("Is the IP %s correct? yes/no (YES): " %{HOST}).lower()
        if (result == 'yes' or result == ''):
            break
        elif (result == 'no'):
            HOST = input("Enter the IP correct: ")
        else:
            print ('Enter a valid answer')

    print (f"\n{'#'*10}   The SSH connection to the server will be established    {'#'*10}\n")
    print (f"\n{'#'*10}    Enter User and Password to complete the connection     {'#'*10}\n")

    client, cmd = ClientSSH.__clientSSH__(HOST)
   
    module = App_Install()

    print (f"\n{'#'*10}   Do you want Step by Step o Unattended installation?     {'#'*10}\n")
    option = input("Write (1) for a Step by Step installatio or (2) for unattended installation: ")

    print (f"\n{'#'*10} Do you want to update the system? yes/no (YES)            {'#'*10}\n")
    UPDATE_SYSTEM = ask()
    if (UPDATE_SYSTEM):
        ClientSSH.__run__(cmd, module.step1.update_system())
    
    print (f"\n{'#'*10} Do you want to install java? yes/no (YES)                 {'#'*10}\n")
    INSTALL_JAVA = ask()
    if (INSTALL_JAVA):
        ClientSSH.__run__(cmd, module.step1.install_java())

    print (f"\n{'#'*10} Do you want to install the basic packages? yes/no (YES)   {'#'*10}\n")
    INSTALL_BASIC_PACKAGES = ask()
    if (INSTALL_BASIC_PACKAGES):
        ClientSSH.__run__(cmd, module.step1.install_packages())

    print (f"\n{'#'*10} Do you want to install Wazuh Manager? yes/no (YES)        {'#'*10}\n")
    INSTALL_WAZUH_MANAGER = ask()
    if (INSTALL_WAZUH_MANAGER):
        if (module.step2.upload_files(HOST)):
            ClientSSH.__run__(cmd, module.step2.install_wazuh())
            ClientSSH.__run__(cmd, module.step2.install_elasticsearch())
            ClientSSH.__run__(cmd, module.step2.install_filebeat())
            ClientSSH.__run__(cmd, module.step2.install_kibana())

    print (f"\n{'#'*10} Do you want to configuring the firewall? yes/no (YES)     {'#'*10}\n")
    CONFIG_FIREWALL = ask()
    if (CONFIG_FIREWALL):
        ClientSSH.__run__(cmd, module.step2.config_firewall())
    
    ClientSSH.__clientSSHclose__(client)

    print (f"\n{'#'*10}           Everything weas installed successfully          {'#'*10}\n")
    print (f"\n{'#'*10}                           ENJOY                           {'#'*10}\n")

    webbrowser.open_new('https://documentation.wazuh.com/4.2/getting-started/')
    webbrowser.open_new('https://'+HOST)
    