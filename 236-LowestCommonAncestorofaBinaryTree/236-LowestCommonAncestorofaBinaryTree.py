# Last updated: 3/26/2025, 10:35:22 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # From a node's perspective, what should we do?
        # at each node, we should check if the values are same as p or q
        # because a node can be LCA of itself, if the current node value is one of
        # p or q then we've found LCA
        # Question is how will we traverse this tree? It's not a binary
        # search tree. 
        # What would be the states? what if we just returned parent of the nodes
        # that we visit and pass that as a state??
        def dfs(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root
            left = dfs(root.left, p , q)
            right = dfs(root.right, p, q)
            if left and not right: # left is p,q right is not
                return left
            if right and not left:
                return right
            if left and right:
                return root
        return dfs(root,p, q)
            
