
class Exceptions():

    def __cmdError__(self, user_cmd):
        if ('incorrect password attempt').encode() in self.cmd_err:
            for line in self.cmd_err.splitlines():
                print (line)
            Exceptions.__incorectPassword(self, user_cmd)
        elif ('[sudo] password for centos: ').encode() in self.cmd_err:
            pass
        else:
            print(f"{'#'*16} Unresolvable Error  {'#'*16}")
            for line in self.cmd_err.splitlines():
                print (line)

    def __incorectPassword(self, user_cmd):
        start = user_cmd.find("-S")
        user_cmd = user_cmd[start+2:]
        prev = "sudo"
        user_cmd = prev+user_cmd
        self.run_cmd(user_cmd)