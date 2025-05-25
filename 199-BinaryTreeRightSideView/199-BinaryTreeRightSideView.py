# Last updated: 5/24/2025, 10:53:20 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # use bfs to traverse through the binary tree
        # O(n) time and space complexity
        if not root:
            return []
        res = []
        queue = deque([root])

        while queue:
            level = len(queue)

            for i in range(level):
                cur = queue.popleft()

                if i == level - 1: # visited all the nodes in this level
                    res.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res