class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lis = []  # Stack to store valid scores
        
        for i in operations:
            if i not in ["C", "D", "+"]:
                # If it's a number, convert to int and add to stack
                lis.append(int(i))
            elif i == "C":
                # Remove the last score
                lis.pop()
            elif i == "D":
                # Double the last score and add to stack
                lis.append(2 * lis[-1])
            elif i == "+":
                # Add the last two scores and push the result
                lis.append(lis[-1] + lis[-2])
        
        # Return the total sum of scores
        return sum(lis)
