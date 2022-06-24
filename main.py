from app.app_install import App_Install
from clientCCmd.ClientSSH import ClientSSH

def progress_bar (progress, total):
    percent = 100 * (progress / float(total))

if __name__ == '__main__':

    HOST='192.168.78.65'
#    HOST='192.168.1.140'
    
    client, cmd = ClientSSH.__clientSSH__(HOST)
    
    module = App_Install()
#    print (module.step1.update)
    ClientSSH.__run__(cmd, module.step1.update)

    ClientSSH.__clientSSHclose__(client)