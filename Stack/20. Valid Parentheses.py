class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for i in s:
            if i in d: #its an closing bracket 
                if len(stack) == 0 or stack[-1] != d[i]: # if stack is empty or the last item in stack is not this baracket companion (sorry)
                    return False 
                else: # means its companion is there so pop
                    stack.pop()
            else: # means its an opening baracket so add it to stack
                stack.append(i)

        if not stack:
            return True
        else:
            return False
