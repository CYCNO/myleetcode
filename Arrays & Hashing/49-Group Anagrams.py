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

# My Attempt with no help

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make all elem sorted in alphabetical order and append it with their index number
        c = []
        for i, elem in enumerate(strs):
            c.append(["".join(sorted(elem)), i])

        d=sorted(c) #sort all the sorted value list
        f =[] # declare final list

        i=0

        #loop through all the elem in d
        while i < len(d):
            temp = [strs[d[i][1]]] # create a temp list and init a the first string 
            #loop until either i get out of range or the sorted chars dont match any more
            while i < len(d) - 1 and d[i][0] == d[i+1][0]:
                temp.append(strs[d[i+1][1]])
                i += 1
            
            # push the temp to the final list
            f.append(temp)
            i+=1
        
        # return final list
        return f
