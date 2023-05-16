class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {} # create a hashmap
        for i in strs:
            sortWord = "".join(sorted(i)) # making them sort from a...z (aet aet )
            if sortWord in dic:
                dic[sortWord].append(i) # adding matching value to the sorted key
            else:
                dic[sortWord] = [i] # adding the new sorted word like key
        return list(dic.values())           
