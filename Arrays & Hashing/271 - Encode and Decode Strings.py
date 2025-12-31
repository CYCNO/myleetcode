# it uses chr() and ord() function of python, its also a mini ceasar cypher
class Solution:
    def encode(self, strs: List[str]) -> str:
        lis = []
        for i in strs:
            for j in i:
                lis.append(chr(ord(j) + 100))
            lis.append("s") # s here represent ,
        return "".join(lis)

    def decode(self, s: str) -> List[str]:
        lis = []
        temp = ""
        for i in s:
            if i == "s":
                lis.append(temp)
                temp = ""
            else:
                temp += chr(ord(i) - 100)
                
        return lis
