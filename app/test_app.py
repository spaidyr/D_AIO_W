from app.app_install import App_Install

class Test_App(App_Install):
    
    def __init__(self) -> None:
        super().__init__()
        self.COMMANDS = ['ls -l',
                    'sudo pwd',
                    'ls -lisah /'
                    ]