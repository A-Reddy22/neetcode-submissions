class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest_substring=0
        
        for num in nums:
            if (num-1) not in nums:
                length=0
                while (num+length) in nums:
                    length+=1
                longest_substring=max(longest_substring, length)
        return longest_substring


            


        