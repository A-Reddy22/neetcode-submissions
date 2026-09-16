class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,high=0,len(nums)-1
        
        while lo<=high:
            mid=((lo+high)//2)
            if nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                lo=mid+1
            elif nums[mid]==target:
                return mid
        return -1