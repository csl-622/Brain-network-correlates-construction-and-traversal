import networkx as nx
import pickle

with open('concept_graph_maxconnected', 'rb') as fp:
	G = pickle.load(fp)


nodeList = list(nx.nodes(G))
edgeList = list(nx.edges(G))
print(len(nodeList))
print(len(edgeList))
for i in range(10):
	print(G.get_edge_data(nodeList[i],nodeList[i+1]))
#shortest_paths_list = {}
#count = 0
#print(len(nodeList)*len(nodeList)/2)
"""
for i in range(len(nodeList)):
	for j in range(i+1,len(nodeList)):
		ij = nx.shortest_path_length(G,source=nodeList[i],target=nodeList[j])
		shortest_paths_list.append(ij)
		count += 1
		print(count)
"""
#print("Max Distance: " + str(max(shortest_paths_list)))
#print("Avg Distance: " + str(sum(shortest_paths_list)/len(shortest_paths_list)))

#paths_list = nx.all_pairs_shortest_path_length(G)
#print("Max Distance: " + str(max(paths_list)))
#print("Avg Distance: " + str(sum(paths_list)/len(paths_list)))
