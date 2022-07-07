import paramiko
import sys
from getpass import getpass
from clientCCmd.Exceptions import Exceptions

class CCmd(object):

    ''' To inject commands is the objective of this class
    '''

    def __init__(self, client):

        ''' The builder method of this class instance differents attributes

            Arguments:
                client: Client SSH which it establish the connection between the user and the server

            Attributes:
                cmd_client: Client SSH which it establish the connection between the user and the server.
                cmd_result: It will be the result of read the stdout of the Linux Terminal.
                cmd_err: It will be the result of read the stderr of the Linux Terminal.
                __SUDO_PASS: this string save the sudo password of the system while the application is execution.
        '''

        self.cmd_client = client
        self.cmd_result = ''
        self.cmd_err = ''
        self.__SUDO_PASS = ''

    def __exec_cmd(self, user_cmd):

        ''' This function execute each command that it is introduce from function run_cmd().
        '''

        if ("sudo -S") in user_cmd:
            pass
        else:
            print(f"\n{'#'*10} Executing the Command: {user_cmd} {'#'*10}")
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
        return self.cmd_result

    def run_cmd(self, __cmd):

        if len(__cmd):
            self.__exec_cmd(__cmd)
        else:
            print('cmd is empty')
            sys.exit(1)           

    def __sudo_cmd(self, __sudoCmd):

        if not self.__SUDO_PASS:
            self.__SUDO_PASS = getpass('Enter your Sudo Password: ')
        prev = 'echo "%s" | ' %self.__SUDO_PASS
        cmd = __sudoCmd.replace("sudo", "sudo -S")
        COMMAND = prev+cmd
        self.__exec_cmd(COMMAND)
        