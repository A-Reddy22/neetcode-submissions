class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we want to create everything to the left of the array and everything to the right of the array
        #we multiply the left of ir and the right of it max 
        left=[]
        right=[]
        new1=[]
        product=1


        for i in range(len(nums)):
            left.append(product)
            product*=nums[i]
        new=1
        for i in range(len(nums)-1,-1,-1):
            right.append(new)
            new*=nums[i]
        
        right.reverse()
            
        total=1
        for i in range(len(nums)):
            total=right[i]*left[i]
            new1.append(total)
        return new1

            
            


        