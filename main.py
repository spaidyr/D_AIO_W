from clientCCmd.ClientSSH import ClientSSH


if __name__ == '__main__':

    HOST='192.168.78.65'
    
    client, cmd = ClientSSH.__clientSSH__(HOST)

    COMMANDS = ['sudo whoami','ls -l']
    ClientSSH.__run__(cmd, COMMANDS)

    ClientSSH.__clientSSHclose__(client)