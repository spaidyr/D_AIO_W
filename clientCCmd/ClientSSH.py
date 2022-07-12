import paramiko
import sys, time
from getpass import getpass
from clientCCmd.CCmd import CCmd

class ClientSSH ():

    ''' This class makes the SSH session which will set the connection between client and server
    '''

    def __clientSSH__(HOST):

        ''' This function builds the objects "client" and "cmd". The object "cmd" permits the user to work with the linux terminal

            Arguments:
                HOST: IP of the server

            Returns:
                client: This object is the client SSH which establishes the connection between the user and the server
                cmd: This object is the Linux Terminal and permit the user to work with the stdin, stdout and stderr of the system
        '''

        try:
            client = ClientSSH.__ssh_client(HOST)
            cmd = CCmd(client)
            return client, cmd
        except Exception:
            sys.exit(1)

    def __clientSSHclose__(client):

        ''' This function closes the client SSH and ends the connection with the server

            Arguments:
                client: It is the client which establishes the connection between the user and the server.
        '''

        client.close()

    def __run__(cmd, COMMANDS):

        ''' This function runs a list of commands and iterates each item or command. This command is introduced and executed in the Linux terminal.

            Arguments:
                cmd: This object is the Linux Terminal and permit the user to work with the stdin, stdout and stderr of the system
                COMMANDS: List of commands.
        '''

        for command in COMMANDS:            
            cmd.run_cmd(command)
            for line in cmd.get_cmd_result().splitlines():
                print (line)
    
    def __ssh_client(HOST):

        ''' This function bulids the Object that is the Client SSH which establishes the connection between the user and the server

            Arguments:
                HOST: IP of the server
            
            Returns:  
                ssh_client: It is the client which establishes the connection between the user and the server.
        '''

        USER = input('User: ')
        PASSWORD = getpass('Password: ')
        try:
            # It starts a client SSH
            ssh_client = paramiko.SSHClient()
            # It makes a policy by default for looking for the key of the local host.
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect
            ssh_client.connect(hostname=HOST, port= 22, username= USER, password= PASSWORD)
        except paramiko.AuthenticationException:
            print("Authentication failed when connecting to %s" % HOST)
            sys.exit(1)
        except:
            print("Failed connection SSH to %s, waiting for it to start" % HOST)
            time.sleep(2)
        return ssh_client