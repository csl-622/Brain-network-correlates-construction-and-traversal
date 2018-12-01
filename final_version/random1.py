from os import listdir
import networkx as nx
import pickle
from multiprocessing import Pool

def create_random_words(fileName,count):
    print(count+1)
    loadString = "processedTestBooks/" + fileName
    print(loadString)
    random_paths = []
    #with open(loadString,'rb') as fp:
        #book_trav = pickle.load(fp)
    #book_trav = list(set(book_trav))
    #n= len(book_trav)
    #print(n)
    #for i in range(len(book_trav)):
    	
            
            
    #saveString = "randomWords/" + str(count+1)
    #with open('saveString', 'wb') as fp:
        #G = pickle.dump(random_paths,fp)


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
        p.starmap(create_random_words,comb_tuples)


def main():
    performTask()

if __name__== "__main__":    
    main()
