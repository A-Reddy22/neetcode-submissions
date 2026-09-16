class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            hash[nums[i]]=i
        

        for i in range(len(nums)):
            value=target-nums[i]
            if value in hash and hash[value]!=i:
                return [i,hash[value]]


        