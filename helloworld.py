import sys
from git import Repo
from jira import JIRA

if JIRA(sys.argv[1]):
  print('can access secret')
else:
  print('cant access secret')
print('hello world')
