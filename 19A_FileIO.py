#!/usr/bin/env python
import sys

if (len(sys.argv)<3):
    print ("E R R O R")
    print (sys.argv[0], ": Invalid usage. \n",sys.argv[0],": Correct usage is:")
    print ('%s %s %s' % (sys.argv[0],"<Input_File>","<Output_File>"))
    sys.exit (1)

inputFile=sys.argv[1]
outputFile=sys.argv[2]


iFile = open(inputFile,'r');
oFile = open (outputFile, 'w');
oFile_2 = open (outputFile + "_Numbered",'w')
iLineNum=0

for eachLine in iFile:
    iLineNum=iLineNum+1
    oFile.write(eachLine)
    oFile_2.write ('%5d %s\n'%(iLineNum,eachLine))

iFile.close()
oFile.close()
oFile_2.close()
