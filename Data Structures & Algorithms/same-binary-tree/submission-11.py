# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue=[p]
        visited=[]
        while queue:
            if queue[0]== None:
                visited.append("null")
            if  queue[0]!= None:
                queue.append(queue[0].left)
                queue.append(queue[0].right)
                
            if queue[0]!= None:
                visited.append(queue[0].val)
            queue.pop(0)
        
        queue1=[q]
        visited1=[]
        while queue1:
            if queue1[0]== None:
                visited1.append("null")
            

            if queue1[0]!= None:
                queue1.append(queue1[0].left)
                queue1.append(queue1[0].right)
            
            if queue1[0]!= None:
                visited1.append(queue1[0].val)
            
            
            queue1.pop(0)

        return visited==visited1
        
        

        