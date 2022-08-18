from pprint import pprint

from testrail import *

client = APIClient('https://rosalindai.testrail.io/')
client.user = 'ibrahim@rosalind.bio'
client.password = 'Rodrigo19!'

case = client.send_get('get_users')
pprint(case)
