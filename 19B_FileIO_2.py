#!/usr/bin/env python
#Print all the cities having population greater than 2m
import sys

try:
    inputFile=sys.argv[1]
except:
    print ("E R R O R")
    print (sys.argv[0], ": Invalid usage. \n Correct usage is:")
    print ('%s %s %s' % (sys.argv[0],"<Input_File>"))
    sys.exit (1)

iFile = open(inputFile,'r');
iLineNum=0

#Data lists:
Cust_ID=[];
Cust_Name=[];
Cust_Population=[];

for eachLine in iFile:
    iLineNum=iLineNum+1
    ID,Name,Count=eachLine.split( '\t')
    Cust_ID.append(ID)
    Cust_Name.append(Name)
    if (int(Count) > 2):
        Cust_Population.append(Count)
    else:
        Cust_Population.append("NOT Important")
iFile.close()

for iCounter in range(0, len(Cust_Population)-1):
  if (not Cust_Population[iCounter] == "NOT Important"):
      print (iCounter, " ", Cust_ID[iCounter], Cust_Name[iCounter],Cust_Population[iCounter])

