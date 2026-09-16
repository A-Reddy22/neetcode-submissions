class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l<r:
            current=0
            mid=(l+r)//2
            for p in range(len(piles)):
                current+= math.ceil(piles[p]/mid)
            
            if current<=h:
                res=min(mid,res)
                r=mid
            elif current>h:
                l=mid+1
        return res

            

        