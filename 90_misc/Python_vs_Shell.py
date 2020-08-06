#!/usr/bin/env python
import os
import sys
Command="dir"
#Run a stand-alone program
failure=os.system(Command)
if failure:
  print ('Could not run', Command); sys.exit(1)

#Redirect output from the application to a list of lines:  
output = os.popen(Command)
res = output.readlines()
output.close()
for line in res:
    print (Command," Output:", line)