# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #so i need to go through each so it is a BFS
        # i will have a queue
        if not root:
            return []
        q=deque([root])
        res=[]
    

        while q:
            levels=[]
            
            for i in range(len(q)):
                node=q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                levels.append(node.val)
            res.append(levels)
        return res
                

        