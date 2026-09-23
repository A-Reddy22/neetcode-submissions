class Solution:
    from collections import Counter
    def singleNumber(self, nums: List[int]) -> int:
        nums_hash=Counter(nums)

        for key,value in nums_hash.items():
            if value!=2:
                return key

        