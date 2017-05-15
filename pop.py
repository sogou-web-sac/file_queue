import sys
import os
import time

records_file= sys.argv[1]
pointer     = sys.argv[2]
n_block     = int(sys.argv[3])

if not os.path.exists(records_file):
  exit(0)

if not os.path.exists(pointer):
  b = 0
else:
  b = int(open(pointer).read().strip())


with open(records_file) as fi:
  i = 0
  for line in fi:
    if i < b:
      i += 1
      continue
    elif i >= b and i < b+n_block:
      print line.strip()
    else:
      break
    i += 1

# reset p_begin
b = i
open(pointer, "wb").write(str(b))

