class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue

            p1=i+1
            p2=len(nums)-1
            while p1<p2:
                # 0=nums1+nums2+nums3
                #nums2+nums3=-nums1
                if nums[p1]+nums[p2]>(-nums[i]):
                    p2-=1
                elif nums[p1]+nums[p2]<(-nums[i]):
                    p1+=1
                elif nums[p1]+nums[p2]==(-nums[i]):
                    ans.append([nums[i],nums[p1],nums[p2]])
                    p1+=1
                    p2-=1
                
                    while p1<p2 and nums[p1]==nums[p1-1]:
                        p1+=1
                    
        return ans

        
        
        