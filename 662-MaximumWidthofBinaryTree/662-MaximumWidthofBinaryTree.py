# Last updated: 6/5/2025, 11:08:48 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque([(root,0)])
        while queue:
            rightPos = -1
            lvl = len(queue)
            _, idx = queue[0]

            for j in range(lvl):
                node,iCur = queue.popleft()
                if j == lvl - 1:
                    rightPos = iCur
                if node.left:
                    queue.append((node.left, iCur * 2 ))
                
                if node.right:
                    queue.append((node.right, iCur * 2 + 1))
            res = max(res, rightPos - idx + 1)
        return res
                
