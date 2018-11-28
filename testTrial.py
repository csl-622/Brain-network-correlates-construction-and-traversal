import pickle
saveString = "processedTestBooks/traversed_book2"
with open(saveString, 'rb') as fp:
	book_data = pickle.load(fp)
	print((book_data))
