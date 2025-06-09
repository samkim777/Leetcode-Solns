# Last updated: 6/8/2025, 11:09:22 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        l = 0

        while queue:
            lvl = len(queue)
            cur = []

            for _ in range(lvl):
                curr = queue.popleft()
                if l % 2 == 0: # RTL
                    cur.append(curr.val)
                else:
                    cur.insert(0,curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            l += 1
            res.append(cur)
        return res


            