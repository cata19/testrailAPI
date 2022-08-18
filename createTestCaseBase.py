from pprint import pprint
from testrail import *

client = APIClient('https://rosalindai.testrail.io/')
client.user = 'ibrahim@rosalind.bio'
client.password = 'Rodrigo19!'

# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://rosalind.atlassian.net/rest/api/3/project"
auth = HTTPBasicAuth("ibrahim@rosalind.bio", "dvwCZhJ9Ysz7LBIu2iF6C219")

headers = {
   "Accept": "application/json",
}

response = requests.request(
   "GET",
   url,
   headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))