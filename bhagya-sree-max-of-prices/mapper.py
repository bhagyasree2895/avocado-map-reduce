import os
input = open("fewRecords.txt", "r")
output = open("01.txt", "w")

for line in input:
    #print(line)
    #sample line of data
    #0,2015-12-27,1.33,64236.62,1036.74,54454.85,48.16,8696.87,8603.62,93.25,0.0,conventional,2015,Albany
    datalist = line.strip().split(",")
    #print(datalist)
    #print(len(datalist))
    serialnum,date,averagePrice,totalvolume, numberOne,numberTwo, numberThree,totalbags,smallbags,largebags,xlargebags,flitertype,year,region = datalist
    output.write(region + "\t" + totalvolume + "\n")

input.close()
output.close()

unsorted = open("01.txt", "r")
sorted = open("02.txt", "w")

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    print (line)
    sorted.write(line)

unsorted.close()
sorted.close()