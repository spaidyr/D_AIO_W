from app.first_config import First_config
from app.wazuh_install import Wazuh_Install

class App_Install:

    ''' 
    The class App_Install initialize the objects which they 
    will load the necesary configuration for deploy the tool
    '''
    
    def __init__(self) -> None:
        self.COMMANDS = ['']
        self.step1 = First_config()
        self.step2 = Wazuh_Install()