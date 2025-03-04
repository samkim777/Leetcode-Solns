# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_sofar):
            if not root:
                return 0
            
            total = 0

            if root.val >= max_sofar:
                total += 1
                max_sofar = root.val
            total += dfs(root.left, max_sofar)
            total += dfs(root.right, max_sofar)
            return total
        return dfs(root, float('-inf'))