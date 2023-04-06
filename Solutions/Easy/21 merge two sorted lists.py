# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      # Initialize dummy linked list as a placeholder
      # dummy.val = 0, and dummy.next = None, as per the constructor above
      dummy = ListNode() 

      # Declare tail to be our instance of linked list
      tail = dummy
      
      # While list1 and list2 not empty
      while list1 and list2:
        # If list2 has greater value node than list1
        # Set our linked list to point towards this lesser node from list1
        if list1.val < list2.val:
          tail.next = list1
          list1 = list1.next
        # Otherwise if list1 has greater value node, do the same with list2  
        else:
          tail.next = list2
          list2 = list2.next
        # Iterate our linked list forward  
        tail = tail.next  

      # If one of the lists empty we exit the while loop

      # Case when list2 is empty  
      if list1:
        # Attach remaining nodes from list1 to our merged linked list
        tail.next = list1
      else:
        # Otherwise if list1 empty, then attach remaining nodes from list2
        # to our merged linked list
        tail.next = list2
      # Since our dummy variable started with value 0, we have to call 
      # dummy.next to return from where the actual head of the merged linked 
      # list is 
      return dummy.next   

