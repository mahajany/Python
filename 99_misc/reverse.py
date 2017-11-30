#!/usr/bin/python3
import sys
s=sys.argv[1]
r=[]  #r=list()
print(s)
for i in s:
    r.append(i)
r.reverse()
s="".join(r)
print(s)
