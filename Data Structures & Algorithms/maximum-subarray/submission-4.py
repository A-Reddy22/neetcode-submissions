class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        new_list = []
        max_sum = float('-inf')  # Initialize max_sum to a very small number
        
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                new_list.append(current_sum)
        
        for value in new_list:
            if value > max_sum:
                max_sum = value
        
        return max_sum

        