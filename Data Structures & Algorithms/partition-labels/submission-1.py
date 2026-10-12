class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap={}
        for i in range(len(s)):
            hashmap[s[i]]=i

        ans=[]
        last=0
        count=0
        for i in range(len(s)):
            last=max(last,hashmap[s[i]])
            count+=1
            if i==last:
                ans.append(count)
                count=0
        return ans
            
