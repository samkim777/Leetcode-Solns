# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def maximumDepth(root):
            if not root:
                return 0
            leftmaxdepth = maximumDepth(root.left)
            rightmaxdepth = maximumDepth(root.right)
            # Not just maximum depth, but need to keep track of maximum diameter    
            diameter = leftmaxdepth + rightmaxdepth
            self.maxDiameter = max(diameter,self.maxDiameter)    
            return 1 + max(leftmaxdepth,rightmaxdepth)        
        maximumDepth(root)
        return self.maxDiameter