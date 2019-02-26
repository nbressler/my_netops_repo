import dotenv
import os
import re
from netmiko import ConnectHandler

dotenv.load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

nxosv = {'device_type': 'cisco_nxos',
		      'ip': '10.0.0.6',
		      'username': USERNAME,
                      'password': PASSWORD}

connection = ConnectHandler(**nxosv)

print("Let's configure both the vlan 1000 interface and the Ethernet1/2 interface")

commands = ['vlan 1000',
	    'interface vlan1000',
	    'desc To ASAv',
	    'ip address 10.255.255.2 255.255.255.240',
	    'no shut',
	    'interface Ethernet1/2',
	    'switchport',
	    'switchport mode trunk',
	    'switchport trunk native vlan 1000',
	    'no shut']

connection.send_config_set(commands)

output = connection.send_command('sh run int Vlan1000')

output = connection.send_command('show ip int Vlan1000 | i Vlan1000')
interface_status = re.match(r'\S+\s+\S+\s+\S+\s+(\S+?)\/(\S+?)\/(\S+?),', output)

if interface_status.group(1).lower == 'protocol-up':
	print('The interface protocol is "UP"!')
else:
	print(f'The interface protocol is "{interface_status.group(1)}"')
if interface_status.group(2).lower == 'link-up':
	print('The interface link is "UP"!')
else:
        print(f'The interface link is "{interface_status.group(2)}"')
if interface_status.group(3).lower == 'admin-up':
        print('The interface is admin "UP"!')
else:
        print(f'The interface is admin "{interface_status.group(3)}"')

