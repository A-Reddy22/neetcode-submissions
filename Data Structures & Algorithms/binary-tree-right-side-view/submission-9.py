# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #using bfs you want to add the last or latest node 
        ans=[]
        q=deque([root])
        if not root:
            return []
        while q:
            trans=[]
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                trans.append(node.val)
            ans.append(trans[-1])
        return ans
        