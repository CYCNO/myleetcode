class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        valS, valT = {},{}
        for i in range(len(s)):
            valS[s[i]] = 1 + valS.get(s[i], 0)
            valT[t[i]] = 1 + valT.get(t[i], 0)
        for i in valS:
            if valS[i] != valT.get(i, 0):
                return False
        return True    
