from app.app_install import App_Install
from clientCCmd.ClientSSH import ClientSSH
from app.test_app import Test_App

if __name__ == '__main__':

    HOST='192.168.78.65'
    
    client, cmd = ClientSSH.__clientSSH__(HOST)
    
    module = App_Install()
    ClientSSH.__run__(cmd, module.step1)

    ClientSSH.__clientSSHclose__(client)