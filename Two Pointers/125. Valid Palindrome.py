class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis = [x.lower() for x in s if x.isalpha() or x.isdigit()] # only get if char in s is either digit or alphabet
        return lis == list(reversed(lis))
