# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we have to take a range
        # so we have (negative infinity, and positive infinity right)
        # so everythong on the left limit is -infinity to the root val
        #everything on the right is right vl to positive infinity

        def dfs(root,left,right):
            if not root:
                return True
            if root.val<=left or root.val>=right:
                return False
            return (dfs(root.left,left, root.val) and
            dfs(root.right,root.val,right))
        return dfs(root,float('-inf'),float('inf'))

        