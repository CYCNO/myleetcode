class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if list dont have any value than it will return nothing
        if len(nums) == 0:
            return 0

        # first sorting the list to compare backward only
        nums.sort()

        # because list is not empty it must have atleast one consecutive element so variable is at one by default
        counter = 1
        max_count = 1


        for i in range(1, len(nums)):

            # if 2 element is same than it will r=continue
            if nums[i] == (nums[i-1]):
                continue

            # if element is 1 bigger than previous one it will update the counter to 1
            elif nums[i] == (nums[i-1] + 1):
                counter += 1
            # if element is not 1 bigger than counter will reset
            else:
                counter = 1

            # pick the biggest counter from max_count or counter and set it to max_count
            #e.g. if counter got only 2 and max counter is 3 than it will be 3 again
            max_count = max(max_count, counter)
        return max_count
