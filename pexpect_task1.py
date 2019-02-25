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

split_output = interface_output.decode().split('\r\n')
print(split_output)
