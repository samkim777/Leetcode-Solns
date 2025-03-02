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
        
        # Find the middle of the LL
        # Rotate from mid to end
        # Merge the two linked lists
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # We've found middle, and the middle.next is beginnign of 2nd half
        second = slow.next
        slow.next = None # split

        # Reverse the second half of the linked list
        prev = None
        while second:
            cur = second.next
            second.next = prev
            prev = second
            second = cur
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            # Now iterate both
            first, second = tmp1, tmp2
            