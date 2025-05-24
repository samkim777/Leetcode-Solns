# Last updated: 5/23/2025, 6:13:59 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Using bfs
        # Time complexity O(n), space is O(n) worst case
        res = []
        queue = deque([root])
        if not root:
            return []

        while queue:
            level_order = []
            curLevel = len(queue)
            # loop through the level
            for _ in range(curLevel):
                curr = queue.popleft()
                level_order.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(level_order)
        return res