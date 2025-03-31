# Last updated: 3/30/2025, 10:23:05 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # binary search tree, return k'th smallest value
        # we can just traverse left, right, and append all values to a list
        # then return k'th (1-indexed, so k-1'th)
        # O(n) time, Space avg O(h), where h height, or O(n) worst case
        # we can use dfs and have a res array
        # base case for dfs will just return None
        # won't need any state
        res = []
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        # We'll have the array in descending order assuming all values unique
        dfs(root)
        return res[k-1]