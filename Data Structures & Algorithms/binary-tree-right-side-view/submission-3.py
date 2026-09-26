from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #binary tree right side view
        # do a bfs traversal
        # do it levels wise but in each level only append -1
        # same as last question but when doing ans.append don't do levels
        #do ans.append[-1]

        if not root:
            return []
        queue=deque([root])
        ans=[]

        while queue:
            levels=[]
            
            for i in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                levels.append(node.val)
            ans.append(levels[-1])
        return ans



        