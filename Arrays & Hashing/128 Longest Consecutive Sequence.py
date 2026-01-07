class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first make sure there is no dublicates so make it set
        numSet = set(nums)
        longest = 0 # track the longest

        for elem in nums: # for every elem in nums
            if (elem - 1) not in numSet: # if it dont have any preceeding value
                largest = 0 
                while (elem + largest) in numSet: # than check how many sequence is after that
                    largest += 1
                longest = max(largest, longest) # change largest if this longest is bigger than previous largest
        return longest
