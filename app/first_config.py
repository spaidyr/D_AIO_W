class First_config():
    
    def __init__(self):
        self.COMMANDS = ['']
        self.update = self.update_system()


    def update_system(self):
        self.COMMANDS = ['sudo yum update -y']
        return self.COMMANDS
