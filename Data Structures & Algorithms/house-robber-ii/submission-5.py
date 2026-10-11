class Solution:
    def rob(self, nums: List[int]) -> int:

        def help(nums):
            rob1=0
            rob2=0
            for i in range(len(nums)):
                temp=max(rob1+nums[i],rob2)
                rob1=rob2
                rob2=temp
            return rob2
        if len(nums)==1:
            return nums[0]

        nums1=nums[1:]
        nums2=nums[:-1]
        return max(help(nums1),help(nums2))
        