from debug_py import *
import pyexpat    #C:\Python33\libs
import uu         #C:\Python33\Lib
#set PYDEBUG=2 to test this script
import os
import sys
debug_py (1,"ONE")
debug_py (2,"TWO")
debug_py (3,"THREE")

try:
    print (os.environ['PYTHONPATH'])
except:
    print ("E R R O R")
    print (sys.argv[0], ": Looks like PYTHONPATH is not an environment variabel here!")

print (sys.path)
       
