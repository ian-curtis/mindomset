import networkx as nx
import sys
from more_itertools import powerset

data_parse = []

for line in sys.stdin.readlines():

  data = line.split()

  data_parse.append((int(data[0]), int(data[1])))
  
print(data_parse)
