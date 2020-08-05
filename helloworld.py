import sys
from git import Repo

arg = sys.argv[1]
print(arg)
f = open(arg)
print(f.readline())
