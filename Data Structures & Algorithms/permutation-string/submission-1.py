from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash=Counter(s1)
        
        l=0
        r=len(s1)
        

        while r<=len(s2):
            new_hash=Counter(s2[l:r])
            if new_hash!=hash:
                r+=1
                l+=1
            else:
                return True
        return False





        