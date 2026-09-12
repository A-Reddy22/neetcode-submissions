class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort the strings, then take the sorted as the key and the value as the unsorted word

        map={}
        sorted_strs=[]
        for i in range(len(strs)):
            sorted_strs.append("".join(sorted(strs[i])))
        for i in range(len(sorted_strs)):
            if sorted_strs[i] in map:
                map[sorted_strs[i]].append(strs[i])
            else:
                map[sorted_strs[i]]=[strs[i]]
        return list(map.values())
        
        
