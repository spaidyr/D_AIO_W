import paramiko
import sys, time
from getpass import getpass
from clientCCmd.CCmd import CCmd

class ClientSSH ():

    def __clientSSH__(HOST):
        try:
            client = ClientSSH.__ssh_client(HOST)
            cmd = CCmd(client)
            return client, cmd
        except Exception:
            sys.exit(1)

    def __clientSSHclose__(client):
        client.close()

    def __run__(cmd, COMMANDS):
        for command in COMMANDS:            
            cmd.run_cmd(command)
            for line in cmd.get_cmd_result().splitlines():
                print (line)
    
    def __ssh_client(HOST):

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