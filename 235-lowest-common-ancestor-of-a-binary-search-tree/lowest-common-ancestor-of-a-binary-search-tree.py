# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # At each node, check current node, left and right 
        # Use the binary tree property: left value is less than current 
        # omg big brain move:
        # 3 cases
        # if both on the left side of node, search left
        # if both on right side of node, search right
        # if on left and right, current node is lca
        def dfs(root, p, q):
            # what about the base case?
            if not root:
                return None
            if root.val > p.val and root.val > q.val: # search left
                return dfs(root.left, p, q)
            elif root.val < p.val and root.val < q.val: # search right
                return dfs(root.right, p, q)
            else:
                return root
        return dfs(root, p, q)