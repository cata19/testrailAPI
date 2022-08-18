from pprint import pprint
from jira import JIRA
from testrail import *
from details import user, password, jiraEmail, token
import json

client = APIClient('https://rosalindai.testrail.io/')
client.user = user
client.password = password
jira = JIRA('https://rosalind.atlassian.net', basic_auth=(jiraEmail, token),
            options={'headers': {"Accept": "application/json"}})

# Set sprint id
sprint_id = 49

# Get Name for New Sprint
sprint = jira.sprint(sprint_id)
pprint(sprint.name)

# Create test suite for current sprint
client.send_post('add_suite/2', {'name': sprint.name, 'description': 'Created using automation PLEASE DELETE'})

# Getting suites as [list] to get the suite id and create a section
suites = client.send_get('get_suites/2')
suite_id = suites[len(suites) - 1]['id']
# print(suite_id)

# Creating a section for the test suite
client.send_post('add_section/2', {'name': 'Automated Test Cases', 'suite_id': suite_id})

# Getting section id to add test cases
sections = client.send_get(f'get_sections/2&suite_id={suite_id}')
section_automated = sections['sections'][0]
section_id = section_automated.get('id')

# Adding cases to test suite
issues = jira.search_issues(f'project = RV4 AND Sprint = {sprint_id}')
for issue in issues:
    client.send_post(f'add_case/{section_id}', {'title': issue.fields.summary, 'refs': issue.key})
    print('{}: {}'.format(issue.key, issue.fields.summary))
