# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Diameter is maximum length of left and right subtrees added
        # Use dfs to recursively calcuate both left and right lengths
        # return value:
        # state: cur heights
        self.diameter = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.diameter = max(self.diameter, left+right)
            return 1 + max(left,right)
        dfs(root)
        return self.diameter
        