import pickle
import networkx as nx
import matplotlib.pyplot as plt
print('Loading Graph')
G = nx.read_weighted_edgelist('merged_edgeList.txt')
print('Saving Graph')
with open('concept_graph', 'wb') as fp: pickle.dump(G, fp)
print('Graph Saved')
