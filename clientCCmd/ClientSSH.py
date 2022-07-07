import paramiko
import sys, time
from getpass import getpass
from clientCCmd.CCmd import CCmd

class ClientSSH ():

    ''' This class make the session SSH which it will set the connection between client and server
    '''

    def __clientSSH__(HOST):

        ''' This function instance the objects "client" and "cmd". The object "cmd" will permit that the user work with the linux terminal

            Arguments:
                HOST: IP of the server

            Returns:
                client: This object is the client SSH which it establish the connection between the user and the server
                cmd: This object is the Linux terminal and permit work with the stdin, stdout and stderr of the system
        '''

        try:
            client = ClientSSH.__ssh_client(HOST)
            cmd = CCmd(client)
            return client, cmd
        except Exception:
            sys.exit(1)

    def __clientSSHclose__(client):

        ''' This function close the client SSH and it finish the connection with the server

            Arguments:
                client: Client SSH which it establish the connection between the user and the server
        '''

        client.close()

    def __run__(cmd, COMMANDS):

        ''' This function run a list of commands and it iterate each item or command. This command will be introduce and execute in the Linux terminal.

            Arguments:
                cmd: The Linux terminal that it permit work with the stdin, stdout and stderr of the system
                COMMANDS: List of commands for CentOS 7.
        '''

        for command in COMMANDS:            
            cmd.run_cmd(command)
            for line in cmd.get_cmd_result().splitlines():
                print (line)
    
    def __ssh_client(HOST):

        ''' This function make the object client that it is the Client SSH which it establish the connection between the user and the server

            Arguments:
                HOST: IP of the server
            
            Returns:  
                ssh_client: Client SSH which it establish the connection between the user and the server
        '''

        USER = input('User: ')
        PASSWORD = getpass('Password: ')
        try:
            # Inicia un cliente SSH
            ssh_client = paramiko.SSHClient()
            # Establecer política por defecto para localizar la llave del host localmente
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Conectarse
            ssh_client.connect(hostname=HOST, port= 22, username= USER, password= PASSWORD)
        except paramiko.AuthenticationException:
            print("Authentication failed when connecting to %s" % HOST)
            sys.exit(1)
        except:
            print("Could not SSH to %s, waiting for it to start" % HOST)
            time.sleep(2)
        return ssh_client