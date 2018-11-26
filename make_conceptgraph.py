import pickle
import networkx as nx
print('Loading File')
with open('nodeDictFile', 'rb') as fp: nodeDict = pickle.load(fp)
print("Files Loaded")
print("Creating Graph")
G = nx.Graph()
print("Graph Created")
print("Adding Vertices")
i = 0
for key, value in nodeDict.items():
    print(i+1)
    G.add_node(key)
    i += 1
print("Vertices Added")
print("Adding Edges")
i = 0
with open("short_merged.txt","r") as f:
    for line in f:
        i = i + 1
        single_esp = line.rstrip().split('\t')
        value = float(single_esp[2])
        G.add_edge(single_esp[0], single_esp[1],weight=value)
        if i%1000 == 0: print(i)
print("Edges Added")    
print('Saving Graph')
with open('concept_graph', 'wb') as fp: pickle.dump(G, fp)
print('Graph Saved')
