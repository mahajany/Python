def foo(x):
    return 1/x

def bar(x):
    try:
        print( foo(x))
    except ZeroDivisionError, message:
        print("Oye! Thou cannot divide by zero:", message)

bar(0)
