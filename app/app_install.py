from app.first_config import First_config
from app.wazuh_install import Wazuh_Install

class App_Install:
    
    def __init__(self) -> None:
        self.COMMANDS = ['']
##        self.step1 = self.first_configuration()
        self.step1 = First_config()
        self.step2 = Wazuh_Install()
    
##    def first_configuration(self):
##        object = First_config()
##        return object

    def test_command(self):
        self.COMMANDS = ['sudo sh -c "echo "-Dlog4j2.formatMsgNoLookups=true" > /etc/elasticsearch/jvm.options.d/disabledlog4j.options"']
        return self.COMMANDS