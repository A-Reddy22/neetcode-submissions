# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d=0

        def height(root):
            if not root:
                return 0
            left= height(root.left)
            right=height(root.right)

            self.max_d=max(self.max_d,left+right)


            return 1+ max(left,right)
        
        height(root)
        return self.max_d
        