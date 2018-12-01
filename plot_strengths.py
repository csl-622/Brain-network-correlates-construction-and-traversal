import networkx as nx
import matplotlib.pyplot as plt
from math import log

strength_list = []
with open('short_merged.txt', 'rb') as fp:
	count = 0
	for line in fp:
		single_esp = line.rstrip().split('\t')
		strength_value = float(single_esp[2])
		strength_list.append(strength_value)
		print(count)
		count += 1

plt.figure(1)
strength_list = [log(x,10) for x in strength_list]
plt.plot(list(range(1,count+1)),strength_list)
plt.xlabel("Word pairs in decreasing oder of strength")
plt.ylabel("Strength of an word pair in terms of log")
plt.show()
