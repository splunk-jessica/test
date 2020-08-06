import sys
import json

list = json.loads(sys.argv[1])
for i in list:
  print(i)
