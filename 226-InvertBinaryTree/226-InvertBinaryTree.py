# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS approach
        def dfs(node):
            # no state to pass from parent to child, and no value to pass from child to parent
            if not node:
                return
            temp = node.right
            node.right = node.left
            node.left = temp
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root