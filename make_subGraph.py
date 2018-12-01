import networkx as nx
import pickle
import matplotlib.pyplot as plt

with open('concept_graph', 'rb') as fp:
	G = pickle.load(fp)

n=10
#print(list(nx.isolates(G)))
'''
largest_components=sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[:n]
for index,component in enumerate(largest_components):
    #nx.draw(component)
    print(str(index)+" "+ str(nx.number_of_nodes(component))+ " "+str(nx.number_of_edges(component)))
    #nx.savefig('fig{}.pdf'.format(index))
    #plt.clf()
    
'''
Gc = max(nx.connected_component_subgraphs(G), key=len)
 
with open('concept_graph_maxconnected', 'wb') as fp: pickle.dump(Gc, fp)
 
print(nx.number_of_nodes(Gc))
print(nx.number_of_edges(Gc))
	
print(nx.is_connected(Gc))

nodeslist = nx.nodes(Gc)

nodeDict = {}
count=0
for key in nodeslist:
	if key not in nodeDict:nodeDict[key]=1
	count +=1
	print(count)
	

print(len(nodeslist))
print(len(nodeDict))


'''

with open('short_merged.txt', encoding='utf-8',errors="ignore") as fp:
    count = 0
    for line in fp:
        single_esp = line.rstrip().split('\t')
        item1 = single_esp[0]
        item2 = single_esp[1]
        if item1 not in nodeDict: nodeDict[item1] = 1
        if item2 not in nodeDict: nodeDict[item1] = 1
        count += 1
        print(count)
        '''
print('Saving File')
with open('nodeDictFile', 'wb') as fp: pickle.dump(nodeDict, fp)
print("The number of nodes in the Graph is " + str(len(nodeDict)))

