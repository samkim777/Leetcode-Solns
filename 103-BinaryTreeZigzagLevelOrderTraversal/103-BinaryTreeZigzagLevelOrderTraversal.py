# Last updated: 6/9/2025, 10:54:55 PM
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
        ltr = 0

        while queue:
            level = len(queue)
            curArr = []
            for _ in range(level):
                curr = queue.popleft()

                if ltr % 2 == 0: # LTR
                    curArr.append(curr.val)
                else:# RTL
                    curArr.insert(0,curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ltr += 1
            res.append(curArr)
        return res