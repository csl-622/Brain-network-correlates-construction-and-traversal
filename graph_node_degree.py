import networkx as nx
import matplotlib.pyplot as plt
import collections
from math import log
G = nx.read_weighted_edgelist('short_merged.txt')
print('Loaded')
nodeList = list(G.nodes())
degreeList = list(G.degree(nodeList).values())
degree_frequency = collections.Counter(degreeList)
degree_frequency_values = [log(x,10) for x in degree_frequency.values()]
degree_frequency_keys = degree_frequency.keys()
print(degree_frequency_keys)
print(degree_frequency_values)
plt.figure(1)
plt.plot(degree_frequency_keys,degree_frequency_values,'.',markersize=10)
plt.xlabel("Node Degree Value")
plt.ylabel("Frequency of Occurence in log")
plt.show()
