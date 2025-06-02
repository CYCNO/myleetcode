class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # create a dic
        counter = {}
        # create max_value var
        max_val = 0
        max_key = None

        # add all the frequency and its perspective numbers in list
        for e in nums:
            if e in counter:
                counter[e] += 1
            else: 
                counter[e] = 1

        # pick the key with most frequency
        for k,v in counter.items():
            if v > max_val:
                max_val = v
                max_key = k
        return max_key
