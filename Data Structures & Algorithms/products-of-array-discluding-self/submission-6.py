class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]
        product=1
        ans=[]
        for i in range(len(nums)):
            prefix.append(product)
            product*=nums[i]
        #postifx
        nums.reverse()
        product=1
        for i in range(len(nums)):
            postfix.append(product)
            product*=nums[i]
        postfix.reverse()
        nums.reverse()

        for i in range(len(nums)):
            ans.append(postfix[i]*prefix[i])
        return ans



        
        

        
            
            
        
        
        
        