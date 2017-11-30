class Stack:
    "A well-known data structure…"
    def __init__(self):		# constructor
        self.items = []
    def push(self, x):
        self.items.append(x)	# the sky is the limit
    def pop(self):
        x = self.items[-1]		# what happens if it’s empty?
        del self.items[-1]
        return x
    def is_empty(self):
        return len(self.items) == 0	# Boolean result
    def clear(self):
        print("...now emptying the stack!")
        self.items = []
    def show(self):
        for i in self.items:
            print(i, end=" ") 
        print()
