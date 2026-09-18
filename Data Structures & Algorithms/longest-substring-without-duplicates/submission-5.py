class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        longest=0
        set1=set()
        l=0
        r=0
        while r<len(s):
            if s[r] not in set1:
                set1.add(s[r])
                r+=1
                length+=1
                longest=max(longest,length)
            else:
                set1.remove(s[l])
                l+=1
                length-=1
        return longest
                
                

            
        
        
        