''' The class First_config initialize the basic configuration of the system '''

class First_config():
    
    def __init__(self):
        self.COMMANDS = ['']
        self.update = self.update_system()
        self.java = self.install_java()

    def update_system(self):
        self.COMMANDS = ['sudo yum update -y']
        return self.COMMANDS

    def install_java(self):
        self.COMMANDS = ['sudo yum install java-11-openjdk-devel -y',
                        'export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar',
                        'echo "export JAVA_HOME=$(dirname $(dirname $(readlink $(readlink $(which javac)))))" >> ./.bashrc',
                        'echo "export PATH=$PATH:$JAVA_HOME/bin" >> ./.bashrc',
                        'echo "export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar" >> ./.bashrc',
                        'source ~/.bashrc',
                        'source ~/.bash_profile']
        return self.COMMANDS
    
    def install_packages(self):
        self.COMMANDS = ['sudo yum install curl unzip wget libcap -y']
        return self.COMMANDS