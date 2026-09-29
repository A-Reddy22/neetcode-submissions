# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #this is a bfs solution I have to traverse it level by level, so queue data structure is used
        q=deque([root])
        ans=[]
        

        while q:
            levels=[]
            
            
            for i in range(len(q)):
                node=q.popleft()
                if not node:
                    return []
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                levels.append(node.val)
            ans.append(levels)
        return ans
            
                
        