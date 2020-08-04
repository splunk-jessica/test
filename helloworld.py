import sys
from createJira import *
from git import Repo

repo = Repo('splunk-jessica/test')
filename = 'splunk-jessica/test/helloworld.py'
diff_output = repo.git.diff(filename)
print(diff_output)

arg = sys.argv[1]
print('hello world')
print(arg)
