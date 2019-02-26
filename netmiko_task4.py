import dotenv
import os
import re
from netmiko import ConnectHandler

dotenv.load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SECRET = os.getenv("SECRET")

asav = {'device_type': 'cisco_asa',
		      'ip': '10.0.0.8',
		      'username': USERNAME,
                      'password': PASSWORD,
		      'secret': SECRET}

connection = ConnectHandler(**asav)

print("Let's start configuring GigabitEthernet0/0")

commands = ['interface GigabitEthernet0/0',
	    'description Connected to CSR',
	    'nameif outside',
            'security-level 0',
            'ip address 203.0.113.2 255.255.255.192',
	    'no shut']

connection.send_config_set(commands)

output = connection.send_command('sh run int GigabitEthernet0/0')
print(output)

print("Let's start configuring GigabitEthernet0/1")

commands = ['interface GigabitEthernet0/1',
	    'description Connected to NX-OSv',
	    'nameif inside',
	    'security-level 100',
	    'ip address 10.255.255.1 255.255.255.240',
	    'no shut']

connection.send_config_set(commands)

output = connection.send_command('sh run int GigabitEthernet0/1')
print(output)

output = connection.send_command('show int ip brief | i GigabitEthernet0/0')
interface_status = re.match(r'\S+\s+\S+\s+\S+\s+\S+\s+(\S+)\s+(\S+)', output)

if interface_status.group(1).lower() == 'up':
	print('The interface status is "UP"!')
else:
	print(f'The interface status is "{interface_status.group(1)}"!')
if interface_status.group(2).lower() == 'up':
	print('The interface protocol is "UP!"')
else:
	print(f'The interface protocol is "{interface_status.group(2)}"!')

output = connection.send_command('show int ip brief | i GigabitEthernet0/1')
interface_status = re.match(r'\S+\s+\S+\s+\S+\s+\S+\s+(\S+)\s+(\S+)', output)

if interface_status.group(1).lower() == 'up':
        print('The interface status is "UP"!')
else:
        print(f'The interface status is "{interface_status.group(1)}"!')
if interface_status.group(2).lower() == 'up':
        print('The interface protocol is "UP!"')
else:
        print(f'The interface protocol is "{interface_status.group(2)}"!')

print("Let's configure our outside route!")

commands = ['route outside 8.8.4.4 255.255.255.255 203.0.113.1']

connection.send_config_set(commands)

output = connection.send_command('show route 8.8.4.4')

if '% Network not in table' in output:
	print('Something went wrong!')
else:
	print('The route was successfully added!')
	print(output)

print ("Let's configure our outside_in ACL!")

commands = ['access-list outside_in extend permit icmp any any',
	    'access-group outside_in in interface outside']

connection.send_config_set(commands)
connection.send_command('wr')
