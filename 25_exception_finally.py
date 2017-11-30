import sys
n=int(sys.argv[1])
try:
    list = 10 * [0]
    if n>11:
        raise IndexError("Raised Exception","Out of range n:"+str(n))
    x = list[n]
    print("Done")
except IndexError as e: 
    print("Index out of bound")
    print(type(e))
    print(e.args)
except Exception as e:
    print("General Exception")
    print(type(e))
    print(e.args)
else: 
    print("Nothing is wrong")
finally: 
    print("Finally we are here")
