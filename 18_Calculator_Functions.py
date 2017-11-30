#calculator program_2: Functions
#this variable tells the loop whether it should loop or not. # 1 means loop. anything else means don't loop.
def menu():
    #print what options you have
    print ("your options are:")
    print ("1) Addition")
    print ("2) Subtraction")
    print ("3) Multiplication")
    print ("4) Division")
    print ("5) Quit calculator.py")
    print (" ")
    return (int(input ("Please choose your option:")))
# this adds two numbers given
def add(a,b):
    print (a, "+", b, "=", int(a) + int(b))
    
# this subtracts two numbers given
def sub(a,b):
    print (b, "-", a, "=", int(b) - int(a))
    
# this multiplies two numbers given
def mul(a,b):
    print (a, "*", b, "=", int(a) * int(b))
    
# this divides two numbers given
def div(a,b):
    print (a, "/", b, "=", int(a) / int(b))
#Actual program: main() 
bLoop = 1
#this variable holds the user's choice in the menu:
iChoice = 0
print ("Welcome to calculator.py")
while bLoop == 1:
    iChoice=menu()
    if iChoice == 1:
          add(input("Add this: "),input("to this: "))
    elif iChoice == 2:
          sub(input("Subtract this: "),input("from this: "))
    elif iChoice == 3:
          mul(input("Multiply this: "),input("by this: "))
    elif iChoice == 4:
          div(input("Divide this: "),input("by this: "))
    elif iChoice == 5:
          bLoop = 0
	
print ("Thank you for using calculator!")
