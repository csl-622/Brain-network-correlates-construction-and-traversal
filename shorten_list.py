import pickle
nodeDict = {}
print("Calculating Average Strength")
with open('merged_edgeList.txt', encoding='utf-8',errors="ignore") as fp:
    count = 0
    total_value = 0
    for line in fp:
        single_esp = line.rstrip().split('\t')
        value = float(single_esp[2])
        total_value = total_value + value
        count += 1
#print(count)
avgValue = total_value/count
print("Average Value of Strength is " + str(avgValue))
print("Shortening Entire List")
eps = []
with open('merged_edgeList.txt', encoding='utf-8',errors="ignore") as fp:
    count = 0
    for line in fp:
        single_esp = line.rstrip().split('\t')
        value = float(single_esp[2])
        if value>=avgValue: eps.append([single_esp[0],single_esp[1],single_esp[2]])
        else: break
        count += 1
        print(count)
fileNameShort = "short_merged.txt"
file = open(fileNameShort,'w+')
for item in eps: file.write(item[0] + '\t' + item[1] + '\t' + item[2] + '\n')

