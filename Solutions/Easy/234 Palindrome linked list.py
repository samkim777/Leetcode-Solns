# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        # Find the mid point
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the pointers to right side starting at mid point
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Check from beginning of list at end of list 
        # prev starts linked list from end of list
        left, right = head, prev
        # right has only left half, so this should be looping condition
        while right:
            if left.val != right.val:
                return False
            left = left.next
            # Reversed, so will iterate r -> l
            right = right.next 
        return True               