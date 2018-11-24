from os import listdir
import re
import pickle
import math
from multiprocessing import Pool
import time



edgePairs = {}
    #strengths = []
count = 0
nodes = []
print(count)
loadString = "edgepair_strength.txt"
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
		temp1 = single_esp[0]
		temp2 = single_esp[1]
		if temp1 not in nodes:
			nodes.append(temp1)
		if temp2 not in nodes:
			nodes.append(temp2)

print(nodes)
print(len(nodes))
#there are 12163 nodes in the gutenberg data list created 


'''
temp = edgePairs
#count +=1
print(count)
count = 0
total = 0
for key in edgePairs:
	count += 1
	total += edgePairs[key]
	#print(" "+str(edgePairs[key])+" ")
mean = total/count	
print("mean "+ str(total/count) +" sum "+ str(total) +" count "+str(count))
count2 = 0
after = {}
for key in edgePairs:
	if edgePairs[key]>=mean:
		count2 +=1
		after[key] = edgePairs[key]
		
count = 0
total = 0
for key in after:
	count += 1
	total += after[key]
	#print(" "+str(edgePairs[key])+" ")
mean = total/count	
print("mean "+ str(total/count) +" sum "+ str(total) +" count "+str(count))	

count2 = 0
after2 = {}
for key in edgePairs:
	if edgePairs[key]>=mean:
		count2 +=1
		after2[key] = after[key]


count = 0
total = 0
for key in after2:
	count += 1
	total += after2[key]
	#print(" "+str(edgePairs[key])+" ")
mean = total/count	
print("mean "+ str(total/count) +" sum "+ str(total) +" count "+str(count))	

count2 = 0
after3 = {}
for key in edgePairs:
	if edgePairs[key]>=mean:
		count2 +=1
		after3[key] = after2[key]


final = 0
for key in after:
	final +=1	
print(final)
print(count2)
'''




	


