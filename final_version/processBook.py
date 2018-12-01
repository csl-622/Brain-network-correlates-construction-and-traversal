from os import listdir
from nltk.stem import WordNetLemmatizer
import re
import pickle
import math
from multiprocessing import Pool
import time

def gethumantime(sec):
    if sec < 60: return str(round(sec,2))+" seconds"
    else: return str(int(sec/60))+" minutes "+str(round(sec%60,2))+" seconds"

def get_stopwords():
    fileOpen = open('stopwords/stopwords.txt',encoding='utf-8',errors="ignore")
    lines = fileOpen.read()
    stopwords = lines.split('\n')
    return(stopwords)

def processBookInformation(fileName,count):
    with open('nodeDictFile', 'rb') as fp:
        nodeDict = pickle.load(fp)
    stopwords = get_stopwords()
    lemmatizer = WordNetLemmatizer()
    folder_name = "testBooks"
    book_data = []
    getfile = open(folder_name+'/'+fileName,encoding='utf-8',errors="ignore")
    lines = getfile.read()
    lines = re.sub('[\\n\\t\\r]+', ' ', lines)
    #eachLine = lines.split('.')
    book_traversed =[]
    lines = re.sub('[^A-Za-z ]+', ' ', lines.lower())
    book_traversed = lines.split(' ')
    book_traversed = list(filter(None,book_traversed))
    book_data = []
    for item in book_traversed:
        if item not in stopwords:
            if item in nodeDict:
                book_data.append(lemmatizer.lemmatize(item))
    getfile.close()
    print("Read Book " + str(count+1))
    saveString = "processedTestBooks/traversed_book" + str(count+1)
    with open(saveString, 'wb') as fp: pickle.dump(book_data, fp)

def performTask():
    st = time.time()
    number_of_workers = 8
    folder_name = "testBooks"
    count = 0
    fileNames = []
    for fileName in listdir(folder_name):
        fileNames.append(fileName)
        count +=1
    comb_tuples = [(fileNames[x],x) for x in range(0,count)]
    with Pool(number_of_workers) as p:
        p.starmap(processBookInformation,comb_tuples)
    et = time.time()
    print("\nIt took "+gethumantime(et-st))

def main():
    performTask()

if __name__== "__main__":    
    main()
