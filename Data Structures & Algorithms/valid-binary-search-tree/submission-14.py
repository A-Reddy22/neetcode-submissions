# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # runnin a recursive basically checking everything on the left is less than parents
        #everything on right is greater than parents


        #dfs on left and right where basically each node should be greater than a certain low value and higher than another value
       
        # runnin a recursive basically checking everything on the left is less than parents
        #everything on right is greater than parents


        #dfs on left and right where basically each node should be greater than a certain low value and higher than another value
        def dfs(root,low,high):
            if not root:
                return True
            if low >=root.val or high<=root.val:
                return False
            return (dfs(root.right,root.val,high) and 
            dfs(root.left,low,root.val))
        return dfs(root,float('-inf'),float('inf'))

            