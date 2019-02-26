import dotenv
import os
import re
from netmiko import ConnectHandler

dotenv.load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

cisco_cloud_router = {'device_type': 'cisco_ios',
		      'ip': '10.0.0.5',
		      'username': USERNAME,
                      'password': PASSWORD}

connection = ConnectHandler(**cisco_cloud_router)

if connection.check_enable_mode():
	print('We are in enable!')
	config_commands = ['interface GigabitEthernet2', 'ip address 203.0.113.1 255.255.255.192', 'no shut']
	connection.send_config_set(config_commands=config_commands)
else:
	print('We are not in enable!')

output = connection.send_command('show run int GigabitEthernet2')
print(output)

output = connection.send_command('show ip int brief')
print(output)

split_lines = output.split('\n')
print(split_lines)

for line in split_lines:
	if 'gigabitethernet2' in line.lower():
		interface_status = re.match(r'\S+\s+\S+\s+\S+\s+\S+\s+(\S+)\s+(\S+)', line)
		if interface_status.group(1).lower() == 'up':
			print('The interface status is "UP"!')
		else:
			print(f'The interface status is "{interface_status.group(1)}"!')
		if interface_status.group(2).lower() == 'up':
			print('The interface protocol is "UP!"')
		else:
			print(f'The interface protocol is "{interface_status.group(2)}"!')

if connection.check_enable_mode():
	print('We are in enable mode again!')
	config_commands = ['ip route 10.255.255.2 255.255.255.255 203.0.113.2']
	connection.send_config_set(config_commands=config_commands)
else:
	print('We are not in eable!')

output = connection.send_command('show ip route 10.255.255.2')
print(output)

if output == '% Network not in table':
	print('Something went wrong!')
else:
	print('The route was successfully added!')
	print(output)
