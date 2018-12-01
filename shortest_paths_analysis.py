from os import listdir
import pickle as pickle

def short_distance_analysis(fileName,count):
    loadString = "distances/" + fileName
    #print(loadString)
    with open(loadString,'rb') as fp:
        distance_trav = pickle.load(fp)
    maxDistance = max(distance_trav)
    avgDistance = sum(distance_trav)/len(distance_trav)
    print("For file " + str(count+1) + " the maximum shortest distance is " + str(maxDistance) + " and the average shortest distance is " + str(avgDistance))
    return(maxDistance,avgDistance)

def performTask():
    number_of_workers = 3
    folder_name = "distances"
    count = 0
    fileNames = []
    for fileName in listdir(folder_name):
        fileNames.append(fileName)
        count +=1
    maxDistance_List = []
    avgDistance_List = []
    for i in range(count):
        [maxDis,avgDis] = short_distance_analysis(fileNames[i],i)
        maxDistance_List.append(maxDis)
        avgDistance_List.append(avgDis)
    with open('maxDistanceList', 'wb') as fp:
        pickle.dump(maxDistance_List,fp)
    with open('avgDistanceList', 'wb') as fp:
        pickle.dump(avgDistance_List,fp)
    	

def main():
    performTask()

if __name__== "__main__":    
    main()
