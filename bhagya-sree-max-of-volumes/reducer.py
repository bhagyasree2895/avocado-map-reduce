#In reducer file max function is applied for the key value pairs
# read input from the file which has few records from actual data pasted into  fewRecords.txt

s = open("02.txt","r")
# write output into the file 01.txt
r = open("03.txt", "w")


# initializing the initial key, values with default values
thisKey = ""
thisValue = 0.0
count=0

# read lines from input one by one 
# read each line using for loop
for line in s:

  # for each line of data strip off the spaces and split using "\t"
  data = line.strip().split('\t')

  # assigning values from the list to the respective variables
  region, totalvolume = data

  # if region is not equal to thiskey enter into the loop
  if region != thisKey:
    # if thiskey has some value(then condition is true) then enter into the if loop
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')
    # start over when changing keys
    thisKey = region 
    thisValue = float(totalvolume)
  # apply the aggregation function - now maximum
  # check if the current total volume is greater than the 
  # existing maximum value update the maximum value with the current total volume
  if (float(totalvolume) > thisValue):
      thisValue =float(totalvolume)
    
# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()