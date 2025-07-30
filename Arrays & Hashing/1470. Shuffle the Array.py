class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        # create new list
        r = []

        # run from zero to n
        for i in range(0, n):
          # first append i than n+1 like( {0,3}, {1,4}, etc
            r.append(nums[i])
            r.append(nums[i+n])
        return r
