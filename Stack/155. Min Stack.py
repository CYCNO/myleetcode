class MinStack:

    def __init__(self):
        self.stack = [] # normal stack
        self.mi = [] # minimum list

    def push(self, val: int) -> None:
        if not self.mi or self.mi[-1] >= val: # if min list is empty or last value of it is same or smaller than it
            self.mi.append(val) # add new value that would act as last min
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.mi[-1]: # when popping check if its also equal to min list
            self.mi.pop() # than pop it too from min list
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mi[-1] # show min last value
