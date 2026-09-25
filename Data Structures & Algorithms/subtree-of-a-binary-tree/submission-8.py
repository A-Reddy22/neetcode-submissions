# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(root,subRoot):
            if not root and not subRoot:
                return True
            if (root and not subRoot) or (subRoot and not root):
                return False
            if root.val!=subRoot.val:
                return False
            

            return same_tree(root.right,subRoot.right) and          same_tree(root.left,subRoot.left)

        if not root and subRoot:
            return False
        if same_tree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))



        
        

        