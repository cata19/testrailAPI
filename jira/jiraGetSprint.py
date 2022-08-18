# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://rosalind.atlassian.net/rest/agile/1.0/sprint/49"
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
