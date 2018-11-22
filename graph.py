import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_weighted_edgelist('edgepairs_n_strength2.txt')
print('Data Loaded')
nodeList = list(G.nodes())
edgeList = list(G.edges())
threshold = 350
removeList = []
print('Removing Weak Components')
for item in edgeList:
    if G.get_edge_data(item[0],item[1])['weight']<threshold: removeList.append(item)
for item in removeList: G.remove_edge(item[0],item[1])
#G.remove_nodes_from(list(nx.isolates(G)))
#removeNodes = [node for node,degree in G.degree().items() if degree < 2]
#G.remove_nodes_from(removeNodes)
print('Getting Max Components')
G = max(nx.connected_component_subgraphs(G), key=len)
print('Drawing')
pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)
plt.show()
