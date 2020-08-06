a,b=0,1
while b < 10:
    print(b)
    print("-----------BEFORE           a,b:",a,b)
    a, b = b, a+b
    print("a, b = b, a+b")
    print("-----------AFTER            a,b:",a,b)
