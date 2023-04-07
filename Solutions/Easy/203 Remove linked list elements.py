# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head) # Start with a node of value 0 pointing
                                      # At our head
        prev,cur = dummy, head

        # We do not need to get rid of pointers in the original head
        # linked list because we are simply adding iteratively to dummy

        while cur:
            nxt = cur.next
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next                