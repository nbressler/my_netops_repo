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

output = connection.send_command('show run int g1')

hostname = connection.find_prompt()
hostname = hostname[:-1]

show_run_int_interface = connection.send_command('show run int g1 | i ^interface')
show_run_int_ip_address = connection.send_command('show run int g1 | i ip address')
show_run_int_description = connection.send_command('show run int g1 | i description')

interface_name = re.match(r'interface\s(.+)', show_run_int_interface)
interface_ip_address = re.match(r'\s+ip address\s(.+)', show_run_int_ip_address)
interface_description = re.match(r'\s+description\s(.+)', show_run_int_description)

if interface_name:
	print(f'Interface Name: {interface_name.group(1)}')
if interface_ip_address:
	print(f'IP Address: {interface_ip_address.group(1)}')
else:
	print('IP Address: N/A')
if interface_description:
	print(f'Description: {interface_description.group(1)}')
else:
	print('Description: N/A')
