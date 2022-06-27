from clientCCmd.ClientSSH import ClientSSH
from local_settings import HOST
from getpass import getpass

class Wazuh_Install():
    
    def __init__(self):
        self.COMMANDS = ['']
        ClientSSH.__sftp_upload__(HOST,'/etc/yum.repos.d/wazuh.repo','./app/files/wazuh.repo', pwd=getpass('Root Password: '))


    def install_wazuh(self):
        
        self.COMMANDS = ['sudo rpm --import https://packages.wazuh.com/key/GPG-KEY-WAZUH',
                        'sudo yum install wazuh-manager-4.2.7-1 -y',
                        'sudo systemctl daemon-reload',
                        'sudo systemctl enable wazuh-manager',
                        'sudo systemctl start wazuh-manager']
        return self.COMMANDS
    
    def install_elasticsearch(self):
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
                        'sudo mv /root/certs/elasticsearch* /etc/elasticsearch/certs/',
                        'sudo mv /root/certs/admin* /etc/elasticsearch/certs/',
                        'sudo cp /root/certs/root-ca* /etc/elasticsearch/certs/',
                        'sudo mkdir -p /etc/elasticsearch/jvm.options.d',
                        'sudo sh -c "echo "-Dlog4j2.formatMsgNoLookups=true" > /etc/elasticsearch/jvm.options.d/disabledlog4j.options"',
                        'sudo chmod 2750 /etc/elasticsearch/jvm.options.d/disabledlog4j.options',
                        'sudo chown root:elasticsearch /etc/elasticsearch/jvm.options.d/disabledlog4j.options',
                        'sudo systemctl daemon-reload',
                        'sudo systemctl enable elasticsearch',
                        'sudo systemctl start elasticsearch',
                        'sudo export JAVA_HOME=/usr/share/elasticsearch/jdk/ && /usr/share/elasticsearch/plugins/opendistro_security/tools/securityadmin.sh -cd /usr/share/elasticsearch/plugins/opendistro_security/securityconfig/ -nhnv -cacert /etc/elasticsearch/certs/root-ca.pem -cert /etc/elasticsearch/certs/admin.pem -key /etc/elasticsearch/certs/admin-key.pem',
                        'sudo /usr/share/elasticsearch/bin/elasticsearch-plugin remove opendistro-performance-analyzer']
        return self.COMMANDS