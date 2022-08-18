from pprint import pprint
from jira import JIRA
from testrail import *
from details import user, password, jiraEmail, token
import json

client = APIClient('https://rosalindai.testrail.io/')
client.user = user
client.password = password

suites = client.send_get('get_suites/2')
suite_id = suites[len(suites) - 1]['id']

sections = client.send_get(f'get_sections/2&suite_id={suite_id}')
section_automated = sections['sections'][0]
section_id = section_automated.get('id')
print(section_id)


# res = [d['name'] for d in suites]
# print(res)
# print(suites[len(suites)-1])