import os
import requests
import dotenv
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
dotenv.load_dotenv()

url = 'https://10.0.0.8/api/'
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

headers = {'Content-Type': 'application/json'}

interface_links = ['interfaces/physical/GigabitEthernet0_API_SLASH_1',
	           'interfaces/physical/Management0_API_SLASH_0',
	           'interfaces/physical/GigabitEthernet0_API_SLASH_8']

for interface_link in interface_links:
	resp = requests.get(f'{url}{interface_link}', auth=(USERNAME, PASSWORD), headers=headers, verify=False)
	resp_dict = json.loads(resp.text)
	payload = "{\n  \"host\": {\n    \"kind\": \"IPv4Address\",\n    \"value\": \"" + resp_dict['ipAddress']['ip']['value'] + "\"\n  },\n  \"kind\": \"object#NetworkObj\",\n  \"name\": \"" + resp_dict['name'] + "\",\n  \"objectId\": \"" + resp_dict['name'] + "\"\n}"
	resp = requests.post(f"{url}objects/networkobjects/{resp_dict['name']}", auth=(USERNAME, PASSWORD), headers=headers, data=payload, verify=False)
	print(resp.status_code)
	print(resp.text)
