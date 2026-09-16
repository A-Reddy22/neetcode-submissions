class Solution:
    def isPalindrome(self, s: str) -> bool:
        p0=0
        p1=(len(s)-1)
        s=s.lower()
        while p0<p1:
            while not s[p1].isalnum() and p0<p1:
                p1-=1
            while not s[p0].isalnum() and p0<p1:
                p0+=1
            
            if s[p0]!=s[p1]:
                return False
            p0+=1
            p1-=1
        return True
            
        
        