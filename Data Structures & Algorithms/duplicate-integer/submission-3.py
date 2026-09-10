class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1={}
        for i in range(len(nums)):
            if nums[i] not in nums1:
                nums1[nums[i]]=1
            else:
                nums1[nums[i]]+=1
        for key,value in nums1.items():
            if value>1:
                return True
        return False

        