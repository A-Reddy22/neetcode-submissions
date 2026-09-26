from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h=Counter(nums)
        array=[0]*(len(nums)+1)

        for key,value in h.items():
            if array[value]==0:
                array[value]=[key]
            else:
                array[value].append(key)

        ans=[]

        for i in range(len(nums),-1,-1):
            if array[i]!=0:
                ans.extend(array[i])
            if len(ans)==k:
                return ans
    

        
        
        

        
        