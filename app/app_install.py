from app.first_config import First_config
from app.wazuh_install import Wazuh_Install

class App_Install:

    ''' 
    The class App_Install initializes the objects which 
    load the necesary configuration to deploy the tool
    '''
    
    def __init__(self) -> None:
        self.COMMANDS = ['']
        self.step1 = First_config()
        self.step2 = Wazuh_Install()