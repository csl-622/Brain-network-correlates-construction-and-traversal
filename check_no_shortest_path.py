import pickle
"""
with open("processedTestBooks/traversed_book43",'rb') as fp:
    book_trav = pickle.load(fp)
book_trav = list(set(book_trav))
k = 0
sq_book = len(book_trav)*len(book_trav)
for i in range(sq_book): print(i,sq_book)
"""
with open("processedTestBooks/traversed_book34",'rb') as fp:
    book_trav = pickle.load(fp)
with open('processedTestBooks/traversed_book34', 'wb') as fp:
        pickle.dump(book_trav,fp,protocol=2)
