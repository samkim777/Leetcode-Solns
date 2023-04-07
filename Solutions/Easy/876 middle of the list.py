# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First grab the length of the entire linked list
        # Then, divide that length by 2
        # Create a for loop and iterate to that middle node
        cur = head
        val = head
        count = 0
        value = 0
        while cur:
            count += 1
            cur = cur.next # Iterate

        for i in range(count // 2):
            value = val.val
            val = val.next

        return val    