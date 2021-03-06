from clientCCmd.ClientSSH import ClientSSH
from getpass import getpass

class Wazuh_Install():

    ''' The class Wazuh_Install loads the necesary configuration for installing Wazuh.
        This object works in the Open Distro version of Elasticsearch
    '''
    
    def __init__(self):

        ''' This function initializes the Object Wazuh_Install. This Object installs and deploys the Wazuh system.
            This object will install the version All-in-One of Wazuh-Manager.
        '''

        self.COMMANDS = ['']

    def install_wazuh(self):

        ''' This function installs Wazuh Manager in the version 4.2. After the installation, this function
            reloads and initializes the services.

            Returns:
                COMMANDS: List of commands in CentOS 7 wihich are necessary for installing wazuh-manager
        '''
        self.COMMANDS = ['sudo rpm --import https://packages.wazuh.com/key/GPG-KEY-WAZUH',
                        'sudo yum install wazuh-manager-4.2.7-1 -y',
                        'sudo systemctl daemon-reload',
                        'sudo systemctl enable wazuh-manager',
                        'sudo systemctl start wazuh-manager']
        return self.COMMANDS
    
    def install_elasticsearch(self):

        ''' This function installs Elasticsearch in the Open Distro version for Wazuh. This process installs Elasticsearch and
            creates the security certificates which implement security for the web navegation. This certificates permit
            that the plataform works in HTTPS.

            Returns:
                COMMANDS: List of commands in CentOS 7 which are necessary for install Elasticsearch.
        '''

        self.COMMANDS = ['sudo yum install opendistroforelasticsearch-1.13.2-1 -y',
                        'sudo curl -so /etc/elasticsearch/elasticsearch.yml https://packages.wazuh.com/resources/4.2/open-distro/elasticsearch/7.x/elasticsearch_all_in_one.yml',
                        'sudo curl -so /usr/share/elasticsearch/plugins/opendistro_security/securityconfig/roles.yml https://packages.wazuh.com/resources/4.2/open-distro/elasticsearch/roles/roles.yml',
                        'sudo curl -so /usr/share/elasticsearch/plugins/opendistro_security/securityconfig/roles_mapping.yml https://packages.wazuh.com/resources/4.2/open-distro/elasticsearch/roles/roles_mapping.yml',
                        'sudo curl -so /usr/share/elasticsearch/plugins/opendistro_security/securityconfig/internal_users.yml https://packages.wazuh.com/resources/4.2/open-distro/elasticsearch/roles/internal_users.yml',
                        'sudo sudo rm /etc/elasticsearch/esnode-key.pem /etc/elasticsearch/esnode.pem /etc/elasticsearch/kirk-key.pem /etc/elasticsearch/kirk.pem /etc/elasticsearch/root-ca.pem -f',
                        'sudo curl -so /root/wazuh-cert-tool.sh https://packages.wazuh.com/resources/4.2/open-distro/tools/certificate-utility/wazuh-cert-tool.sh',
                        'sudo curl -so /root/instances.yml https://packages.wazuh.com/resources/4.2/open-distro/tools/certificate-utility/instances_aio.yml',
                        'sudo bash /root/wazuh-cert-tool.sh',
                        'sudo mkdir /etc/elasticsearch/certs/',
                        'sudo mv /root/certs/elasticsearch.pem /etc/elasticsearch/certs/',
                        'sudo mv /root/certs/elasticsearch-key.pem /etc/elasticsearch/certs/',
                        'sudo mv /root/certs/admin.pem /etc/elasticsearch/certs/',
                        'sudo mv /root/certs/admin-key.pem /etc/elasticsearch/certs/',
                        'sudo cp /root/certs/root-ca.pem /etc/elasticsearch/certs/',
                        'sudo cp /root/certs/root-ca-key /etc/elasticsearch/certs/',
                        'sudo mkdir -p /etc/elasticsearch/jvm.options.d',
                        'sudo sh -c "echo "-Dlog4j2.formatMsgNoLookups=true" > /etc/elasticsearch/jvm.options.d/disabledlog4j.options"',
                        'sudo chmod 2750 /etc/elasticsearch/jvm.options.d/disabledlog4j.options',
                        'sudo chown root:elasticsearch /etc/elasticsearch/jvm.options.d/disabledlog4j.options',
                        'sudo systemctl daemon-reload',
                        'sudo systemctl enable elasticsearch',
                        'sudo systemctl start elasticsearch',
                        'sudo export JAVA_HOME=/usr/share/elasticsearch/jdk/',
                        'sudo /usr/share/elasticsearch/plugins/opendistro_security/tools/securityadmin.sh -cd /usr/share/elasticsearch/plugins/opendistro_security/securityconfig/ -nhnv -cacert /etc/elasticsearch/certs/root-ca.pem -cert /etc/elasticsearch/certs/admin.pem -key /etc/elasticsearch/certs/admin-key.pem',
                        'sudo /usr/share/elasticsearch/bin/elasticsearch-plugin remove opendistro-performance-analyzer']
        return self.COMMANDS

    def install_filebeat (self):

        ''' This function installs Filebeat in the version 7.10 of Elasticsearch. Filebeat is necessary for wazuh to work correctly.
            This function takes the certificates made in the function 'def install_elasticsearch()'. Filebeat won't work without
            these certificates.

            Returns:
                COMMANDS: List of commands in CentOS 7 which are necessary for installing Filebeat.
        '''

        self.COMMANDS = ['sudo yum install filebeat-7.10.2-1 -y',
                        'sudo curl -so /etc/filebeat/filebeat.yml https://packages.wazuh.com/resources/4.2/open-distro/filebeat/7.x/filebeat_all_in_one.yml',
                        'sudo curl -so /etc/filebeat/wazuh-template.json https://raw.githubusercontent.com/wazuh/wazuh/4.2/extensions/elasticsearch/7.x/wazuh-template.json',
                        'sudo chmod go+r /etc/filebeat/wazuh-template.json',
                        'sudo wget https://packages.wazuh.com/4.x/filebeat/wazuh-filebeat-0.1.tar.gz',
                        'sudo tar -xvzf wazuh-filebeat-0.1.tar.gz -C /usr/share/filebeat/module',
                        'sudo mkdir /etc/filebeat/certs',
                        'sudo cp /root/certs/root-ca.pem /etc/filebeat/certs/',
                        'sudo mv /root/certs/filebeat.pem /etc/filebeat/certs/',
                        'sudo mv /root/certs/filebeat-key.pem /etc/filebeat/certs/',
                        'sudo systemctl daemon-reload',
                        'sudo systemctl enable filebeat',
                        'sudo systemctl start filebeat']
        return self.COMMANDS
    
    def install_kibana (self):

        ''' This function install Kibana in the Open Distro version.  
        '''

        self.COMMANDS = ['sudo yum install opendistroforelasticsearch-kibana -y',
                        'sudo curl -so /etc/kibana/kibana.yml https://packages.wazuh.com/resources/4.2/open-distro/kibana/7.x/kibana_all_in_one.yml',
                        'sudo mkdir /usr/share/kibana/data',
                        'sudo chown -R kibana:kibana /usr/share/kibana/data',
                        'sudo -u kibana /usr/share/kibana/bin/kibana-plugin install https://packages.wazuh.com/4.x/ui/kibana/wazuh_kibana-4.2.6_7.10.2-1.zip',
                        'sudo mkdir /etc/kibana/certs',
                        'sudo cp /root/certs/root-ca.pem /etc/kibana/certs/',
                        'sudo mv /root/certs/kibana.pem /etc/kibana/certs/',
                        'sudo mv /root/certs/kibana-key.pem /etc/kibana/certs/',
                        'sudo chown kibana:kibana /etc/kibana/certs/*',
                        'sudo setcap "cap_net_bind_service=+ep" /usr/share/kibana/node/bin/node',
                        'sudo systemctl daemon-reload',
                        'sudo systemctl enable kibana',
                        'sudo systemctl start kibana']
        return self.COMMANDS
    
    def config_firewall (self):

        ''' This function configures the firewall of CentOS to permit the incoming HTTPS traffic.
        '''

        self.COMMANDS = ['sudo firewall-cmd --add-service=https',
                        'sudo firewall-cmd --runtime-to-permanent']
        return self.COMMANDS

    def repo_wazuh (self):

        ''' This function makes the file with the configuration of the repository of Wazuh v4.
        '''

        self.COMMANDS = ['touch wazuh.repo',
                        'echo "[wazuh]" >> wazuh.repo',
                        'echo "gpgcheck=1" >> wazuh.repo',
                        'echo "gpgkey=https://packages.wazuh.com/key/GPG-KEY-WAZUH" >> wazuh.repo',
                        'echo "enabled=1" >> wazuh.repo',
                        'echo "name=EL-\$releasever - Wazuh" >> wazuh.repo',
                        'echo "baseurl=https://packages.wazuh.com/4.x/yum/" >> wazuh.repo',
                        'echo "protect=1" >> wazuh.repo',
                        'sudo chown root:root wazuh.repo',
                        'sudo mv wazuh.repo /etc/yum.repos.d/',
                        'sudo chmod 644 /etc/yum.repos.d/wazuh.repo']
        return self.COMMANDS