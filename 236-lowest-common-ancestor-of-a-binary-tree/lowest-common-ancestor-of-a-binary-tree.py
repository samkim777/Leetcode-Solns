# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Case 1: if p,q found in left, right, return current root
        # Case 2: If p,q both found in left or right subtree, then return p or q 
        # Time complexity: Average would be O(h), Worst case would be O(n)
        # Space complexity would be similar
        def dfs(root, p, q):
            if not root:
                return None
            # Case 1:
            if root == q or root == p:
                return root
            # if both left and right subtrees have p,q, return current root
            left = dfs(root.left, p,q)
            right = dfs(root.right, p,q)
            if left and right:
                return root
            if left and not right:
                return left
            if right and not left:
                return right
            else:
                return None
        return dfs(root,p,q)