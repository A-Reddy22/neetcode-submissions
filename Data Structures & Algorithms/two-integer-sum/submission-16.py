class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            a[nums[i]]=i


        for i in range(len(nums)):
            needed=target-nums[i]
            if needed in a and a[needed]!=i:
                return [i,a[needed]]


        