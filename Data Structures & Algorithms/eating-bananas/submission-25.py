import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #find the minimum number of banans to finish in h hours
        # use binary search where the high=max of piles
        #low is 0
        l=1
        r=max(piles)

        while l<r:
            mid=((l+r)//2)
            current=0
            i=0
            for i in range(len(piles)):
                current+=math.ceil(piles[i]/mid)
            if current>h:
                l=mid+1
            else:
                r=mid
        return r



        