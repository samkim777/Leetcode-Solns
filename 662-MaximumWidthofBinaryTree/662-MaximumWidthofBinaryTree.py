# Last updated: 6/11/2025, 10:58:18 PM
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
        curMax = 0
        while queue:
            level = len(queue)
            cudIdx = 0
            _, idx = queue[0]
            for _ in range(level):
                node, curIdx = queue.popleft()
                if node.left:
                    queue.append([node.left, 2 * curIdx])
                if node.right:
                    queue.append([node.right, 2 * curIdx + 1])
                
            res = max(res, curIdx - idx + 1)
        return res
