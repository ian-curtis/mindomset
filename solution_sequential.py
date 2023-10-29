import networkx as nx
import sys
from more_itertools import powerset

data_parse = []

# read in data
for line in sys.stdin.readlines():

  data = line.split()

  data_parse.append((int(data[0]), int(data[1])))

n_towns = data_parse[0][0]
n_pairs = data_parse[0][1]

towns = list(range(n_towns))
pairs = list(range(n_pairs))

print(f"You entered {n_towns} towns with {n_pairs} connections.\n")

# extract all of the inputted connected towns
connections = data_parse[1:]

# Create graph representation of connections
G = nx.Graph()
G.add_nodes_from(range(n_towns))
G.add_edges_from(connections, length = 1)

if not nx.is_connected(G):
  print("Not all towns are connected! You won't get reliable results.\n")

# create the powerset (list of all possible subsets)
subsets = list(powerset(towns))

dom_sets = []

# this loop could be parallelized
# checks if a subset is a dominating set, if so, sets it aside
for i in range(1, len(subsets)):

  dom_set = nx.is_dominating_set(G, list(subsets[i]))

  if dom_set:
    dom_sets.append(subsets[i])

dom_sets.sort(key = len)

stations_needed = len(dom_sets[0])

towns_as_stations = ""

for town in dom_sets[0]:
  if len(towns_as_stations) == 0:
    towns_as_stations += str(town)
  else:
    continue_str = ", " + str(town)
    towns_as_stations += continue_str

print(f"The number of stations needed is {stations_needed}.\nTown IDs: {towns_as_stations}")