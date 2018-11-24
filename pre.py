from os import listdir
import re
import pickle
import math
from multiprocessing import Pool
import time


def get_stopwords():
	fileOpen = open('stopwords/stopwords.txt',encoding='utf-8',errors="ignore")
	lines = fileOpen.read()
	stopwords = lines.split('\n')
	return(stopwords)
	
	
def processBookInformation(fileName,count):
	stopwords_preprocessing()
	stopwords = get_stopwords()
	lemmatizer = WordNetLemmatizer()
	folder_name = "inputBooks"
	cut_size = 7
	#list of all books containing sentenced token words
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
		new_token_words = []
	  #list of all token words in a sentences
		for each_tokenWords in token_words:
	  		if each_tokenWords not in stopwords:
	  			new_token_words.append(lemmatizer.lemmatize(each_tokenWords))
		list_sentences.append(new_token_words)
	book_data = list_sentences
	getfile.close()
	print("Read Book " + str(count+1))
	saveString = "tokenized_books/tokenized_book" + str(count+1)
	with open(saveString, 'wb') as fp: pickle.dump(book_data, fp)

