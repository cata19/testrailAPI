from jira import JIRA
from testrail import *
from details import user, password, jiraEmail, token

client = APIClient('https://rosalindai.testrail.io/')
client.user = user
client.password = password
# jira = JIRA()

jira = JIRA('https://rosalind.atlassian.net', basic_auth=( jiraEmail, token), options={'headers': {"Accept": "application/json"}})

# Calling issues from current sprint
issues_in_sprint = jira.search_issues('project = RV4 AND status in (In-Progress, Open)AND Sprint = 49')

# Adding section to test suite
# client.send_post('add_section/2', {'name': 'Automated Test Cases', 'suite_id': '138'})

# Creating test cases for current sprint OPEN and IN-PROGRESS
#for issue in issues_in_sprint:
    #client.send_post('add_case/733', {'title': issue.fields.summary, 'refs': issue.key})
    #print('{}: {}'.format(issue.key, issue.fields.summary))

issues = jira.search_issues('project = RV4 AND Sprint = 49')
for issue in issues:
    client.send_post('add_section/2', {'name': 'Automated Test Cases', 'suite_id': '138'})
    client.send_post('add_case/733', {'title': issue.fields.summary, 'refs': issue.key})
    print('{}: {}'.format(issue.key, issue.fields.summary))