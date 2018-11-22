from os import listdir
from nltk.stem import WordNetLemmatizer
import re
import pickle
import math

def gaussianStrength(wordGap):
    strength = math.exp(-wordGap)
    return(strength)

def stopwords_preprocessing():
    fileOpen = open('stopwords/unprocessed_stopwords.txt',encoding='utf-8',errors="ignore")
    lines = fileOpen.read()
    fileOpen.close()
    fileOpen = open('stopwords/stopwords.txt','w+',encoding='utf-8',errors="ignore")
    eachLine = lines.split('\n')
    stopwords = list(set(eachLine))
    for i in range(len(stopwords)): stopwords[i] = re.sub('[^A-Za-z]+', '', stopwords[i].lower())
    stopwords = list(set(stopwords))
    stopwords.sort()
    for i in range(len(stopwords)): 
        if i == len(stopwords)-1: fileOpen.write(stopwords[i])
        else: fileOpen.write(stopwords[i]+'\n')
    fileOpen.close()
    
def get_stopwords():
    fileOpen = open('stopwords/stopwords.txt',encoding='utf-8',errors="ignore")
    lines = fileOpen.read()
    stopwords = lines.split('\n')
    return(stopwords)

def processBookInformation():
    stopwords_preprocessing()
    stopwords = get_stopwords()
    lemmatizer = WordNetLemmatizer()
    folder_name = "test"
    cut_size = 7
    count = 0
      #list of all books containing sentenced token words
    for fileName in listdir(folder_name):
        book_data = []
        getfile = open(folder_name+'/'+fileName,encoding='utf-8',errors="ignore")
        lines = getfile.read()
        lines = re.sub('[\\n\\t\\r]+', ' ', lines)
        eachLine = lines.split('.')
        list_sentences =[]  #list of all sentences of token words
        for index in range(len(eachLine)):
            eachLine[index] = re.sub('[^A-Za-z ]+', ' ', eachLine[index].lower())
        eachLine = list(filter(None, eachLine))
        new_eachLine = []
        for data in eachLine:
            data_token = data.split(' ')
            data_token = list(filter(None, data_token))
            chunks = [data_token[x:x+cut_size] for x in range(0, len(data_token), cut_size)]
            new_eachLine.extend(chunks)
        eachLine = new_eachLine
        eachLine = list(filter(None, eachLine))
        for index in range(len(eachLine)):
            token_words = eachLine[index]
            #token_words = list(filter(None, token_words))
            new_token_words = []    #list of all token words in a sentences
            for each_tokenWords in token_words:
                if each_tokenWords not in stopwords:
                    new_token_words.append(lemmatizer.lemmatize(each_tokenWords))
            list_sentences.append(new_token_words)
        book_data = list_sentences
        getfile.close()
        count += 1
        print("Read Book " + str(count))
        saveString = "t_books/tokenized_book" + str(count)
        with open(saveString, 'wb') as fp: pickle.dump(book_data, fp)
    return(new_eachLine,count)
    
def calculate_strength(count):
    #with open('tokenized_book', 'rb') as fp: book_data = pickle.load(fp)
    disp_count = 1
    #print(count)
    for book_index in range(count):
        edgePairs = []
        strengths = []
        loadString = "tokenized_books/tokenized_book" + str(disp_count)
        with open(loadString, 'rb') as fp: eachBook = pickle.load(fp)
        print(disp_count)
        for source_sentence in range(len(eachBook)):
            for source_word in range(len(eachBook[source_sentence])):
                wordGap = 0
                index = source_word + 1
                for dest_word in range(index,len(eachBook[source_sentence])):
                    item_pair = [eachBook[source_sentence][source_word],eachBook[source_sentence][dest_word]]
                    wordGap = wordGap + 1
                    conceptStrength = gaussianStrength(wordGap)
                    if item_pair not in edgePairs:
                        edgePairs.append(item_pair)
                        strengths.append(conceptStrength)
                    else:
                        i = edgePairs.index(item_pair)
                        strengths[i] = strengths[i] + conceptStrength
                        
        eps = []
        for i in range(len(edgePairs)): eps.append([edgePairs[i][0],edgePairs[i][1],strengths[i]])
        #eps.sort(key=lambda elem: elem[2],reverse=True)
        fileNameEP = "edgepairs/edgepair_strength_"+str(disp_count)+".txt" 
        file = open(fileNameEP,'w+')
        for i in range(len(edgePairs)):
            if i<len(edgePairs): file.write(str(eps[i][0]) + '\t\t' + str(eps[i][1]) + '\t\t' + str(eps[i][2]) + '\n')
            else: file.write(str(eps[i][0]) + '\t\t' + str(eps[i][1]) + '\t\t' + str(eps[i][2]) + '\n')
        file.close()
        disp_count +=1

def merge_edges():
    edgePairs = {}
    #strengths = []
    count = 1
    folder_name = "edgepairs"
    for fileName in listdir(folder_name):
        print(count)
        loadString = "edgepairs/edgepair_strength_" + str(count) + ".txt"
        with open(loadString, encoding='utf-8',errors="ignore") as fp:
            for line in fp:
                single_esp = line.rstrip().split('\t\t')
                value = float(single_esp[2])
                item_pair = single_esp[0] + "\t" +single_esp[1]
                if item_pair in edgePairs:
                    edgePairs[item_pair] = edgePairs[item_pair] + value
                else:
                    edgePairs[item_pair] = value
        count +=1
    eps = []
    for key, value in edgePairs.items():
        eps.append([key,value])
    eps.sort(key=lambda elem: elem[1],reverse=True)
    fileNameEP = "merged_edgeList.txt" 
    file = open(fileNameEP,'w+')
    for i in range(len(edgePairs)):
        if i<len(edgePairs): file.write(str(eps[i][0]) + '\t' + str(eps[i][1]) + '\n')
        else: file.write(str(eps[i][0]) + '\t' + str(eps[i][1]) + '\n')
    file.close()

def performTask():    
    [newLine,count] = processBookInformation()
    count = 3036
    calculate_strength(count)
    merge_edges()
    
performTask()
