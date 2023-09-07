from pprint import pprint
from jira import JIRA
from testrail import *
from details import user, password, jiraEmail, token

# Testrail Credentials
client = APIClient('https://rosalindai.testrail.io/')
client.user = user
client.password = password

# Jira Credentials
jira = JIRA('https://rosalind.atlassian.net', basic_auth=(jiraEmail, token),
            options={'headers': {"Accept": "application/json"}})

# Set sprint id
sprint_id = 49  # jira sprint id
project_id = 2  # testrail project id

# Get Name for New Sprint from Jira
sprint = jira.sprint(sprint_id)
pprint(sprint.name)

# Create test suite for current sprint inside Testrail
client.send_post(f'add_suite/{project_id}', {'name': sprint.name, 'description': 'Retro Example'})

# Getting a list of test suites to get the newest suite id in order to create a section inside the test suite
suites = client.send_get(f'get_suites/{project_id}')
suite_id = suites[len(suites) - 1]['id']
# print(suite_id)

# Creating a section for the test suite in Testrail
client.send_post(f'add_section/{project_id}', {'name': 'Automated Test Cases', 'suite_id': suite_id})

# Getting the first section id to add test cases
sections = client.send_get(f'get_sections/{project_id}&suite_id={suite_id}')
section_automated = sections['sections'][0]
section_id = section_automated.get('id')

# Adding cases to test suite
issues = jira.search_issues(f'project = RV4 AND Sprint = {sprint_id}')
for issue in issues:
    client.send_post(f'add_case/{section_id}', {'title': issue.fields.summary, 'refs': issue.key})
    print('{}: {}'.format(issue.key, issue.fields.summary))
