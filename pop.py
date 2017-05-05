import sys
import os
import time

seeds_all = sys.argv[1]
pointer   = sys.argv[2]
n_split   = int(sys.argv[3])

if not os.path.exists(seeds_all):
  exit(0)

urls = open(seeds_all).read().strip().split("\n")
n_block = len(urls) / n_split

if not os.path.exists(pointer):
  p_begin = 0
else:
  p_begin = int(open(pointer).read().strip())

if p_begin + n_block <= len(urls):
  p_end = p_begin + n_block
else:
  p_end = len(urls)


for i in xrange(p_begin, p_end):
  print urls[i]

# reset p_begin
p_begin = p_end
open(pointer, "wb").write(str(p_end))
