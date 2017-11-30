#!/usr/bin/env python
#Demonstrate
#how to read a command-line argument
#how to call a math (sine) function
#how to work with variables
#how to print text and numbers
# load system and math module:
import sys, math
# extract the 1st command-line argument:
r=0
if len(sys.argv)>1:
   r = float(sys.argv[1])
s = math.sin(r)
print ( "Hello, World! sin(" + str(r) + ")=" + str(s) )
