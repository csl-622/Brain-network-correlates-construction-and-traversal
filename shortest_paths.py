from os import listdir
import networkx as nx
import pickle
from multiprocessing import Pool

def calc_short_distances(fileName,count):
    #print(count+1)
    
    loadString = "processedTestBooks/" + fileName
    print(loadString)
    with open('concept_graph_maxconnected', 'rb') as fp:
        G = pickle.load(fp)
    shortest_paths = []
    with open(loadString,'rb') as fp:
        book_trav = pickle.load(fp)
    book_trav = list(set(book_trav))
    for i in range(len(book_trav)):
        for j in range(i+1,len(book_trav)):
            #try:
            shortest_paths.append(nx.shortest_path(G,source=book_trav[i],target=book_trav[j]))
            #except nx.NetworkXNoPath:
                #c = 0
    saveString = "distances/" + str(count+1)
    with open('saveString', 'wb') as fp:
        G = pickle.dump(shortest_paths,fp)

def performTask():
    number_of_workers = 3
    folder_name = "processedTestBooks"
    count = 0
    fileNames = []
    for fileName in listdir(folder_name):
        fileNames.append(fileName)
        count +=1
    comb_tuples = [(fileNames[x],x) for x in range(0,count)]
    with Pool(number_of_workers) as p:
        p.starmap(calc_short_distances,comb_tuples)


def main():
    performTask()

if __name__== "__main__":    
    main()
