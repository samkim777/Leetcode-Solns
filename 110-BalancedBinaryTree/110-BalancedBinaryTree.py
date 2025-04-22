# Last updated: 4/21/2025, 10:18:43 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # calculate the left and right subtree heights
        # if differ by greater than 1, return False
        # O(n) time, O(h) avg space, O(n) worst space
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                return -1
            if left == -1 or right == -1:
                return -1
            return 1 + max(left,right)
        return dfs(root) != -1