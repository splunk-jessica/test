import sys
from git import Repo

f = open('README.md')
print(f.readline())

arg = sys.argv[1]
print('hello world')
if arg:
  print('can access secret')
