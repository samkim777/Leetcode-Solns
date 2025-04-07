# Last updated: 4/6/2025, 11:49:20 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Dfs, find the min difference later
        res = []
        def dfs(root):
            if not root:
                return None
            # In-order traversal
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        # res is sorted array
        dfs(root)
        min_diff = float("inf")
        for i in range(1, len(res)):
            min_diff = min(min_diff, abs(res[i] - res[i - 1]))
        return min_diff