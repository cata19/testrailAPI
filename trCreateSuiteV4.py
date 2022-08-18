from pprint import pprint
from details import user, password
from testrail import *

client = APIClient('https://rosalindai.testrail.io/')
client.user = user
client.password = password

# result = client.send_post('add_suite/2', {'name': 'Sprint 11 (6.6.5)', 'description': 'this is a test'})

result = client.send_get('get_projects&is_completed=0')
pprint(result)


