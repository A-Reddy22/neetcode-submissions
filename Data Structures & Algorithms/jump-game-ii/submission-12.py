class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r=0,0
        jumps=0
    
        for i in range(len(nums)-1):
            r=max(r,nums[i]+i )

            if i==l:
                jumps+=1
                l=r
        

        return jumps

        