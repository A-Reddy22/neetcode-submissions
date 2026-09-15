class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        max_substring=0
        curr=0
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i]-1==nums[i-1]:
                curr+=1
            if curr>max_substring:
                max_substring=curr
            if nums[i]-1!=nums[i-1]:
                curr=0
        
        return max_substring+1
        
            


        