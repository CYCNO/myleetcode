class MinStack:
    # we need min value in 0(1) so we also added minLis
    def __init__(self):
        self.lis = []
        self.minLis = []

    def push(self, val: int) -> None:
        self.lis.append(val) # add in normal value
        if len(self.minLis) == 0 or val <= self.minLis[-1]: # if minLis not exist than append a value and make it exist or 
          # if value value is smaller than the smallest (or last) value of minLis than also append
            self.minLis.append(val)

    def pop(self) -> None:
        val = self.lis.pop() # pop normal lis value
        if val == self.minLis[-1]:# if value popping in normal is also the min value or last value of minLis than pop it 
            self.minLis.pop()

    def top(self) -> int:
        return self.lis[-1] # get top from normal lis

    def getMin(self) -> int:
        return self.minLis[-1] # get smallest or last value from minLis
