# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        cur = head

        while cur:
            if cur not in visited:
                visited.add(cur)
                cur = cur.next
            else:
                return True
        return False 