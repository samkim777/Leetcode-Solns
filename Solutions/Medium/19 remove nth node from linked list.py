# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        left,right = dummy,dummy

        for i in range(n + 1):
            right = right.next

        # Right is pointing n distances away from left
        # *** Don't need to check edge cases
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next     

        return dummy.next   