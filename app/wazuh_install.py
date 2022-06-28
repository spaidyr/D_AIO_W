from clientCCmd.ClientSSH import ClientSSH
from settings import HOST
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
        self.COMMANDS = ['sudo firewall-cmd --add-service=https',
                        'sudo firewall-cmd --runtime-to-permanent']
        return self.COMMANDS