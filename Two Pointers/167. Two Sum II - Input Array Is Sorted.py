class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1 
        left = 0
        while True:
            su = numbers[right] + numbers[left]
            if su == target:
                return [left + 1, right +1]
                break
            elif su > target:
                right -= 1
            elif su < target:
                left += 1
