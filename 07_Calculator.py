#calculator program
#this variable tells the loop whether it should loop or not. # 1 means loop. anything else means don't loop.
bLoop = 1
#this variable holds the user's choice in the menu:
iChoice = 0
print ("Welcome to calculator.py")
while bLoop == 1:
    #print what options you have
    print ("your options are:")
    print ("1) Addition")
    print ("2) Subtraction")
    print ("3) Multiplication")
    print ("4) Division")
    print ("5) Quit calculator.py")
    print (" ")
    iChoice=int(input("Choose your option: "))
    print ("You entered >>" , iChoice , "<<")	
	
    if iChoice == 1:
        print ("Addition")
        add1 = int(input("Add this: "))
        add2 = int(input("to this: "))
        print (add1, "+", add2, "=", add1 + add2 )
    elif iChoice == 2:
        print ("Subtraction")	
        sub2 = int(input("Subtract this: "))
        sub1 = int(input("from this: "))
        print (sub1, "-", sub2, "=", sub1 - sub2)
    elif iChoice == 3:
        print ("Multiplication")	
        mul1 = int(input("Multiply this: "))
        mul2 = int(input("with this: "))
        print (mul1, "*", mul2, "=", mul1 * mul2)
    elif iChoice == 4:
        print ("Division")
        div1 = int(input("Divide this: "))
        div2 = int(input("by this: "))
        print (div1, "/", div2, "=", div1 / div2)
    elif iChoice >= 5:
        bLoop = 0
	
print ("Thankyou for using calculator.py!")
