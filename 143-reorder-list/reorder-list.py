# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 3 steps:
        # 1) Find the mid point of the linked list
        # 2) Reverse starting from that mid point
        # 3) Merge the two halves in order
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # Reverse the half
        prev = None
        while second:
            cur = second.next
            second.next = prev
            prev = second
            second = cur
        
        # merge the two
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2
        
