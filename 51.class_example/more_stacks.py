from stack import *
class FancyStack(Stack):
    "stack with added ability to inspect inferior stack items"

    def peek(self, n):
        "peek(0) returns top; peek(-1) returns item below that; etc."
        size = len(self.items)
        assert 0 <= n < size			# test precondition
        return self.items[size-1-n]

class LimitedStack(FancyStack):
    "fancy stack with limit on stack size"

    def __init__(self, limit):
        self.limit = limit
        FancyStack.__init__(self)		# base class constructor

    def push(self, x):
        assert len(self.items) < self.limit
        FancyStack.push(self, x)		# "super" method call
