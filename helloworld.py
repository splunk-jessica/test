import sys
from git import Repo
from jira import JIRA

if sys.argv[1]:
  print('can access secret')
else:
  print('cant access secret')
print('hello world')
