import networkx 
import pickle
import matplotlib.pyplot as plt

with open('concept_graph', 'rb') as fp:
	G = pickle.load(fp)

n=10
largest_components=sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[:n]
for index,component in enumerate(largest_components):
    nx.draw(component)
    nx.savefig('fig{}.pdf'.format(index))
    plt.clf()

	
print(networkx.is_connected(G))
