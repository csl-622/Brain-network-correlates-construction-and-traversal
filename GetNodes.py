import pickle
nodeDict = {}
with open('short_merged.txt', encoding='utf-8',errors="ignore") as fp:
    count = 0
    for line in fp:
        single_esp = line.rstrip().split('\t')
        item1 = single_esp[0]
        item2 = single_esp[1]
        if item1 not in nodeDict: nodeDict[item1] = 1
        if item2 not in nodeDict: nodeDict[item1] = 1
        count += 1
        print(count)
print('Saving File')
with open('nodeDictFile', 'wb') as fp: pickle.dump(nodeDict, fp)
print("The number of nodes in the Graph is " + str(len(nodeDict)))
