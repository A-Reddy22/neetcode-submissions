class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r=0,0
        jumps=0

        for i in range(len(nums)-1):
            r=max(nums[i]+i,r)

            if i==l:
                l=r
                jumps+=1
        return jumps
        