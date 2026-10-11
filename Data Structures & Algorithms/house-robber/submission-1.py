class Solution:
    def rob(self, nums: List[int]) -> int:
        #when we are at a point we can either rob that point and i-2 or we can rob the point before so we have tow choices one is to rob that point and i-2 before and the second is to take up just the point ebfore
        #so at a point i we need i-1 and i-2
        rob1,rob2=0,0
        for i in range(len(nums)):
            temp=max(rob1+nums[i], rob2)
            rob1=rob2
            rob2=temp
        return temp
    
        