class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        if len(nums) == 1:
            return True
        current_jump=nums[0]


        while current_jump>0:
            if current_jump>0:
                i+=1
                current_jump-=1
            if current_jump<nums[i]:
                current_jump=nums[i]
            if i>=len(nums)-1:
                return True
        return False
            

        