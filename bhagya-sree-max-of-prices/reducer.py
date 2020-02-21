s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0
count=0

for line in s:
  data = line.strip().split('\t')
  region, totalvolume = data
  if region != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')
    # start over when changing keys
    thisKey = region 
    thisValue = float(totalvolume)
  # apply the aggregation function - now maximum
  # thisValue += float(totalvolume)
  #print(thisKey + '\t' + str(thisValue)+'\n')
  if (float(totalvolume) > thisValue):
      thisValue =float(totalvolume)
    
# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')
#print("count ",count)


s.close()
r.close()