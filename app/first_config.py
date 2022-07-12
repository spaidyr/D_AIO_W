class First_config():

    ''' The class First_config initializes the basic configuration of the system '''
    
    def __init__(self):

        ''' This function initializes the object type First_config.
        '''

        self.COMMANDS = ['']

    def update_system(self):

        ''' This function updates the system
        '''

        self.COMMANDS = ['sudo yum update -y']
        return self.COMMANDS

    def install_java(self):

        ''' This function installs and configures Java.
            Java is necessary for installing the Elastic STACK
        '''

        self.COMMANDS = ['sudo yum install java-11-openjdk-devel -y',
                        'export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar',
                        'echo "export JAVA_HOME=$(dirname $(dirname $(readlink $(readlink $(which javac)))))" >> ./.bashrc',
                        'echo "export PATH=$PATH:$JAVA_HOME/bin" >> ./.bashrc',
                        'echo "export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar" >> ./.bashrc',
                        'source ~/.bashrc',
                        'source ~/.bash_profile']
        return self.COMMANDS
    
    def install_packages(self):

        ''' This section installs the different packets which are necessary for the system to work correctly.
        '''

        self.COMMANDS = ['sudo yum install curl unzip wget libcap -y']
        return self.COMMANDS