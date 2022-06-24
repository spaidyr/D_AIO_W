from app.first_config import First_config

class App_Install:
    
    def __init__(self) -> None:
        self.COMMANDS = ['']
        self.step1 = self.first_configuration()
    
    def first_configuration(self):
        object = First_config()
        return object