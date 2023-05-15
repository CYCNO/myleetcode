class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_list = set()
        for i in nums:
            if i in check_list:
                return True
            check_list.add(i)
        return False
