from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Start with the first unique element at index 0, so k=1
        # 'k' will point to the next position to place a unique element
        k = 1

        # Iterate over the array starting from index 1
        for i in range(1, len(nums)):
            # If the current element is different from the last unique one
            if nums[i] != nums[k - 1]:
                # Place it at index 'k' (next position for a unique value)
                nums[k] = nums[i]
                # Move k forward
                k += 1

        # 'k' is the number of unique elements, and
        # the first k elements in nums are now the unique values
        return k
