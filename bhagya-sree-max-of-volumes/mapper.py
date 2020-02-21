#mapper file is used extract to the required key value pairs and sorting them
# read input from the file which has few records from actual data pasted into  fewRecords.txt
input = open("fewRecords.txt", "r")
# write output into the file 01.txt
output = open("01.txt", "w")

# read lines from input one by one 
# read each line using for loop
for line in input:
    #sample line of data
    #0,2015-12-27,1.33,64236.62,1036.74,54454.85,48.16,8696.87,8603.62,93.25,0.0,conventional,2015,Albany

    # for each line of data strip off the spaces and split using ","
    datalist = line.strip().split(",")

    # assigning values from the list to the respective variables
    serialnum,date,averagePrice,totalvolume, numberOne,numberTwo, numberThree,totalbags,smallbags,largebags,xlargebags,flitertype,year,region = datalist

    # saving the key-value pairs in to the output file seperated by \t
    output.write(region + "\t" + totalvolume + "\n")

# closing the opened input and output files
input.close()
output.close()


# sortshuffle.py
# opening file 01.txt for reading
unsorted = open("01.txt", "r")
# opening file 02.txt for writing
sorted = open("02.txt", "w")

# readlines from the input file which is unsorted data
dataList = unsorted.readlines()

# sort lines from the datalist
dataList.sort()

# read each line from sorted datalist 
for line in dataList:
    # print (line)
    # write each line into the sorted file
    sorted.write(line)
   
# closing the opened input unsorted file and output sorted files
unsorted.close()
sorted.close()