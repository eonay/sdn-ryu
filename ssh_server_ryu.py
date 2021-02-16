import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.88.111',username='root',password='root')
ssh.exec_command('kldload carp')
ssh.exec_command('ifconfig em0 inet vhid 1 pass senhasecreta alias 192.168.88.123/32 up')
ssh.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
ssh.close()

ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect(hostname='192.168.88.222',username='root',password='root')
ssh2.exec_command('kldload carp')
ssh2.exec_command('ifconfig em0 inet vhid 1 pass senhasecreta alias 192.168.88.123/32 up')
ssh2.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
ssh2.close()
