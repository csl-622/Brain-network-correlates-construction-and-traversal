from os import listdir
import pickle
import networkx as nx
import time
import random
from multiprocessing import Pool

def gethumantime(sec):
    if sec < 60: return str(round(sec,2))+" seconds"
    else: return str(int(sec/60))+" minutes "+str(round(sec%60,2))+" seconds"

def get_adjacent_distances(fileName,count):
	loadString = "processedTestBooks/traversed_book" + str(count+1)
	with open(loadString, 'rb') as fp:
		book_data = pickle.load(fp)
	with open('concept_graph_maxconnected', 'rb') as fp:
		G = pickle.load(fp)
	get_len = len(book_data)
	adj_path_len_list = []
	get_distance_factor = 5
	#traversed_index = 0
	for i in range(0,get_len-get_distance_factor,get_distance_factor):
		get_source_node = book_data[i]
		get_destination_node = book_data[i + get_distance_factor]
		adj_path_len = nx.shortest_path_length(G,source=get_source_node,target=get_destination_node)
		adj_path_len_list.append(adj_path_len)
		#traversed_index = traversed_index + get_distance_factor
	saveString = "adj_Distances/traversed_book_path" + str(count+1)
	with open(saveString, 'wb') as fp: pickle.dump(adj_path_len_list, fp)
	print("Traversed Book" + str(count+1) + "   " + str(len(adj_path_len_list)))
	
def generate_random_number_list(count):
	random_sizeList = []
	with open('concept_graph_maxconnected', 'rb') as fp:
		G = pickle.load(fp)
	nodeList = list(nx.nodes(G))
	for i in range(count):
		r_no = random.randint(100,100000)
		random_sizeList.append(r_no)
	for i in range(count):
		random_pick1 =  random.choice(nodeList)
		random_node_list = []
		random_node_list.append(random_pick1)
		random_node_distance_list = []
		for j in range(random_sizeList[i]):
			random_pick2 = random.choice(nodeList)
			adj_path_len = nx.shortest_path_length(G,source=random_pick1,target=random_pick2)
			random_node_distance_list.append(adj_path_len)
			random_pick1 = random_pick2
			random_node_list.append(random_pick1)
		saveString = "random_node_list/nodeSet" + str(i+1)
		with open(saveString, 'wb') as fp: pickle.dump(random_node_list, fp)
		saveString = "random_node_distance_list/distanceSet" + str(i+1)
		with open(saveString, 'wb') as fp: pickle.dump(random_node_distance_list, fp)
		print("Generated Sequence " + str(i+1))
	
def performTask():
	st = time.time()
	number_of_workers = 8
	folder_name = "processedTestBooks"
	count = 0
	fileNames = []
	for fileName in listdir(folder_name):
		fileNames.append(fileName)
		count +=1
	comb_tuples = [(fileNames[x],x) for x in range(0,count)]
	with Pool(number_of_workers) as p:
		p.starmap(get_adjacent_distances,comb_tuples)
	generate_random_number_list(count)
	et = time.time()
	print("\nIt took "+gethumantime(et-st))

def main():
	performTask()

if __name__== "__main__":    
	main()
