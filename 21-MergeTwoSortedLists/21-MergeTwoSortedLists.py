# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy linked list
        dummy = ListNode()

        # In order to maintain pointer in the correct position for dummy, create another pointer
        tail = dummy

        # At each node, compare and set the next of dummy accordingly
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        
        # If any of the lists are non-empty, attach remaining nodes to dummy
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next