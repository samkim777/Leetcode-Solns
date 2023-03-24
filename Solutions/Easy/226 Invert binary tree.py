# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:        # If empty tree return 
            return 

        temp = root.left 
        root.left = root.right # Swap left and right
        root.right = temp      # Swap right and left
        self.invertTree(root.left) # Recurse through left of root
        self.invertTree(root.right)# Recurse through right of root

        return root    