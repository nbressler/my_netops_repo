import dotenv
import os
import pexpect
import re

dotenv.load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
device_ip = "10.0.0.5"

connection = pexpect.spawn(f'ssh {USERNAME}@{device_ip}')

connection.expect('Password:')
connection.sendline(PASSWORD)

print(connection.before)
print(connection.after)

connection.expect('ignw-csr#')

print(connection.before)
print(connection.after)

matchObj = re.match(r'b\'(.*)\#', (connection.after).decode())

if matchObj:
	print(matchObj.group(1))

connection.sendline('show run interface g1')
connection.expect('ignw-csr#')

interface_output = connection.before
print(interface_output)

#split_output = interface_output.decode().split('\r\n')
#print(split_output)

#for config_item in split_output:
#	if config_item.startswith('interface'):
#		print(config_item)
#	if config_item.startswith(' description'):
#		print((config_item).lstrip())
#	if config_item.startswith(' ip address'):
#		print((config_item).lstrip())

interface_name = re.findall(r'interface.([A-Z,a-z]*?Ethernet[^\r])', (interface_output).decode())
interface_description = re.findall(r'description[^\r]*', (interface_output).decode())

print(interface_name[0])
print(interface_description)
