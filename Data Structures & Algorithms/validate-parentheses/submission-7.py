class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])

            if s[i]==")" and len(stack)>0 and stack[-1]=="(":
                stack.pop()
            elif s[i]==")"  and len(stack)>0 and stack[-1]!="(" or s[i]==")" and len(stack)<=0:
                return False

            if s[i]=="]"and len(stack)>0 and stack[-1]=="[":
                stack.pop()
            elif s[i]=="]" and len(stack)>0 and stack[-1]!="[" or s[i]=="]" and len(stack)<=0:
                return False


            if s[i]=="}" and len(stack)>0 and stack[-1]=="{":
                stack.pop()
            elif s[i]=="}" and len(stack)>0 and stack[-1]!="{" or s[i]=="}" and len(stack)<=0:
                return False
        return len(stack)==0
                

        