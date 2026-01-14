class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxValue = 0
        l,r = 0,len(heights) - 1 # setting up pointers

        while l < r: # so they dont meet each other
            width = r - l # difference between both 
            
            # check which one is smaller
            minHeight = min(heights[l], heights[r])
            
            # add the value in maxValue if its bigger
            maxValue = max(minHeight * width, maxValue)
            
            # now if h[l] is smaller than move l to right because we need bigger value 
            if heights[l] < heights[r]:
                l += 1
            else:
                r-=1
        return maxValue
