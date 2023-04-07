# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use linked list's value!
        cur = head
        while(cur):
            if(cur.val is None):
                return True
            cur.val = None
            cur = cur.next

        return False    

