#!/usr/bin/python3
import sys
def main():
    try:
        f()
        print("After the function call")
    except ZeroDivisionError:
        t=sys.exc_info()
        ####print(sys.last_value())
        print(t[0])
        ####print(sys.last_type())
        print(t[1])
        #####print(sys.last_traceback())
        print(t[2])
        print("Divided by zero!")
    except:
        print("Exception")
        print("---------")

def f(): 
    print(1 / 0)

if __name__ == "__main__":
   main()
