from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Count=Counter(nums)
        val=[0]*(len(nums)+1)

        for key,value in Count.items():
            if val[value]==0:
                val[value]=[key]
            else:
                val[value].append(key)
        
        res=[]
        ans=[]
        for i in range(len(nums),-1,-1):
            if val[i]!=0:
                res.extend(val[i])
            if len(res)==k:
                return res
            
        
        
        

        
        