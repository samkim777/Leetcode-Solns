# Last updated: 4/10/2025, 10:33:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Each "level" needs to be a separate array
        res = []
        def dfs(root, level):
            if not root:
                return None
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root,0)
        return res