from clientCCmd.ClientSSH import ClientSSH

if __name__ == 'main':

    HOST = '192.168.44.130'

    client, cmd = ClientSSH.__clientSSH__(HOST)

    COMMANDS = ['ls -l']
    ClientSSH.__run__(cmd, COMMANDS)

    ClientSSH.__clientSSHclose__(client)