from os import listdir
import networkx as nx
import pickle as pickle
from multiprocessing import Pool

def calc_short_distances(fileName,count):
    
    loadString = "processedTestBooks/" + fileName
    print(loadString)
    with open('concept_graph_maxconnected', 'rb') as fp:
        G = pickle.load(fp)
    shortest_paths = []
    with open(loadString,'rb') as fp:
        book_trav = pickle.load(fp)
    book_trav = list(set(book_trav))
    k = 0
    for i in range(len(book_trav)):
        for j in range(i+1,len(book_trav)):
            #try:
            shortest_paths.append(nx.shortest_path_length(G,source=book_trav[i],target=book_trav[j]))
            k += 1
            if k%100000 == 0:
            	print(k,len(book_trav)*(len(book_trav)-1)/2)
    saveString = "distances/distance" + str(count+1)
    with open(saveString, 'wb') as fp:
        pickle.dump(shortest_paths,fp)

def performTask():
	number_of_workers = 3
	folder_name = "processedTestBooks"
	count = 0
	fileNames = []
	for fileName in listdir(folder_name):
		fileNames.append(fileName)
		count +=1
	for i in range(count):
		calc_short_distances(fileNames[i],i)
		print(i+1)
    	

def main():
    performTask()

if __name__== "__main__":    
    main()
