import os
import dotenv
import xml.dom.minidom
from ncclient import manager

dotenv.load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

m = manager.connect(host='10.0.0.5', port=830, username=USERNAME, password=PASSWORD, device_params={'name': 'csr'})

for thing in m.server_capabilities:
	print(thing)

#print(dir(m))

config = m.get_config(source='running')

#print(config)

print(xml.dom.minidom.parseString(config.xml).toprettyxml())
