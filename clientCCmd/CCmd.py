import paramiko
import sys
from getpass import getpass
from clientCCmd.Exceptions import Exceptions

class CCmd(object):

    ## Clase de comando de ejecución remota

    def __init__(self, client):
        self.cmd_client = client
        self.cmd_result = ''
        self.cmd_err = ''
        self.__SUDO_PASS = ''

    def __exec_cmd(self, user_cmd):

        if ("sudo -S") in user_cmd:
            print(f"\n{'#'*10} Executing the Command {'#'*10}\n")
        else:
            print(f"\n{'#'*10} Executing the Command: {user_cmd} {'#'*10}\n")
        try:
            if user_cmd.startswith('sudo '):
                self.__sudo_cmd(user_cmd)
            else:
                self.cmd_err = ''

                stdin, stdout, stderr = self.cmd_client.exec_command(user_cmd)
                self.cmd_result = stdout.read()
                self.cmd_err = stderr.read()
                if self.cmd_err:
                    if not ("[sudo] password for centos: ").encode() in self.cmd_err:
                        self.__SUDO_PASS = ''
                    Exceptions.__cmdError__(self, user_cmd)                      
        except paramiko.PasswordRequiredException:
            print('Password requerida')
            
    def get_cmd_result(self):
        ## Devolvemos el resultado de la ejecución del comando
        return self.cmd_result

    def run_cmd(self, __cmd):

        ## Ejecutamos el comando
        if len(__cmd):
            self.__exec_cmd(__cmd)
        else:
            print('cmd is empty')
            sys.exit(1)           

    def __sudo_cmd(self, __sudoCmd):

        ## Trasformación del comando SUDO
        if not self.__SUDO_PASS:
            self.__SUDO_PASS = getpass('Enter your Sudo Password: ')
        prev = 'echo "%s" | ' %self.__SUDO_PASS
        cmd = __sudoCmd.replace("sudo", "sudo -S")
        COMMAND = prev+cmd
        self.__exec_cmd(COMMAND)
        