class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the array so problem become just like two sum ii
        res = []

        # loop over all element
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # if before elem is same as now skip it
                continue
            l, r = i+1, len(nums) - 1 # set pointers

            while l < r: # while they dont meet each other
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -=1 # if it is greater than 0 than move right one less down, because its sorted so moving it back will decrease the value and will be closer to 0
                elif threeSum < 0:
                    l +=1 # same logic for left but this time we increase it
                else:
                    res.append([a, nums[l], nums[r]]) # append if its equal to zero
                    l += 1 # increase the pointer more
                    while l < r and nums[l] == nums[l-1]: # left shouldn't be equal to it's previous one if it is than increase left pointer
                        l+=1

        return res
