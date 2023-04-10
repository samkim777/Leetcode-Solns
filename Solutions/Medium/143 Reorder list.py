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

        slow, fast = head,head

        # Find the middle point
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        ## Logic here?    
        second = slow.next 
        prev = slow.next = None
        # Reversed half the list
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        first,second = head,prev    
        # Iterate through and merge the two lists
        while second:
            temp,rtemp = first.next, second.next
            first.next = second
            second.next = temp
            first = temp
            second = rtemp      
