class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # what i am thinking of doing is sorting the string
        #and then add it ig

        #so maybe what i do is i sort everything then
        # first need to sort it
        array=[]
        ans=[]
        hashmap={}

        for i in range(len(strs)):
            array.append("".join(sorted(strs[i])))
        
        for i in range(len(array)):
            if array[i] in hashmap:
                hashmap[array[i]].append(strs[i])
            else:
                hashmap[array[i]]=[strs[i]]
        for key,value in hashmap.items():
            ans.append(value)
        return ans


        

        