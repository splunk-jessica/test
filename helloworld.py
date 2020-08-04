import sys
from git import Repo

repo = Repo('test')
filename = 'test/helloworld.py'
diff_output = repo.git.diff(filename)
print(diff_output)

arg = sys.argv[1]
print('hello world')
print(arg)
