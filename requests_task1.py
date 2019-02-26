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

resp = requests.get(f'{url}interfaces/physical', auth=(USERNAME, PASSWORD), verify=False)

#print(resp)
#print(resp.status_code)
#print(dir(resp))

resp = requests.get(f'{url}interfaces/physical', auth=(USERNAME, PASSWORD), verify=False)
resp_dict = json.loads(resp.text)
#print(resp_dict)

ints_qty = resp_dict['rangeInfo']['total']
ints_names = []

for i in resp_dict['items']:
	ints_names.append(i['hardwareID'])

print(f'The ASAv has {ints_qty} interfaces. Named as follows:')
for ints_name in ints_names:
	print(ints_name)
