class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # get position and speed in pair
        st = [[x,y] for x, y in zip(position,speed)]
        st.sort(reverse=True) # sort pair w.r.t position
        tt=[] # create a stack for time taken

        for p, s in st: # in reverse order (position higher to lower)
            tt.append((target-p)/s) # append time of cars
            if len(tt) >= 2 and tt[-1] <= tt[-2]: # if car is slower from next it's next car 
                tt.pop() # than remove it from stack

        return len(tt) # return the length of stack which have every time greater than its next one
