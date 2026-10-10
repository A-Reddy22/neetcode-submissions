class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        
        ans=[0]*(len(nums)+1)
        for key,value in freq.items():
            if ans[value]==0:
                ans[value]=[key]
            else:
                ans[value].append(key)
        final=[]
        for i in range(len(nums),-1,-1):
            if ans[i]!=0:
                final.extend(ans[i])
            if len(final)==k:
                return final
        