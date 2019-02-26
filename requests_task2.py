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

payload = '''
{
	"host": {
		"kind": "IPv4Address",
		"value": "8.8.8.8"
	},
	"kind": "object#NetworkObj",
	"name": "leGoogle",
	"objectId": "leGoogle"
}
'''
#print(payload)

headers = {'Content-Type': 'application/json'}

resp = requests.post(f'{url}objects/networkobjects/leGoogle', auth=(USERNAME, PASSWORD), headers=headers, data=payload, verify=False)

print(resp.status_code)
print(resp.text)
