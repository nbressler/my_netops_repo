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
	config_commands = ['interface loopback 0', 'ip address 172.16.1.1 255.255.255.255']
	connection.send_config_set(config_commands=config_commands)
else:
	print('We are not in enable!')

output = connection.send_command('show run int l0')
print(output)

output = connection.send_command('show ip int brief')
print(output)

split_lines = output.split('\n')
print(split_lines)

for line in split_lines:
	if 'loopback0' in line.lower():
		interface_status = re.match(r'\S+\s+\S+\s+\S+\s+\S+\s+(\S+)\s+(\S+)', line)
		if interface_status.group(1).lower() == 'up':
			print('The interface stats is "UP!"')
		if interface_status.group(2).lower() == 'up':
			print('The interface protocol is "UP!"')

if connection.check_enable_mode():
	print('We are in enable mode again!')
	config_commands = ['interface loopback 1', 'ip address 8.8.4.4 255.255.255.255']
	connection.send_config_set(config_commands=config_commands)
else:
	print('We are not in eable!')

output = connection.send_command('show run int l1')
print(output)

output = connection.send_command('show ip int brief')
print(output)

split_lines = output.split('\n')
print(split_lines)

for line in split_lines:
        if 'loopback1' in line.lower():
                interface_status = re.match(r'\S+\s+\S+\s+\S+\s+\S+\s+(\S+)\s+(\S+)', line)
                if interface_status.group(1).lower() == 'up':
                        print('The interface stats is "UP!"')
                if interface_status.group(2).lower() == 'up':
                        print('The interface protocol is "UP!"')
