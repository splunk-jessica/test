import sys
from git import Repo

f = open('README.md')
print(f.readline())

arg = sys.argv[1]
print('this is from Branch splunk-jessica-patch-1')
print(arg)
