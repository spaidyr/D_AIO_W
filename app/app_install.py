class App_Install:
    
    def __init__(self) -> None:
        self.COMMANDS = ['']
        self.step1 = self.config_init()
    
    def config_init(self):
        self.COMMANDS = ['ls -l',
                        'sudo pwd',
                        'ls -lisah /'
                        ]
        return self.COMMANDS