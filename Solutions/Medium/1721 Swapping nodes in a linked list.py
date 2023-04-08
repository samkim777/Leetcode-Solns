# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # The list is 1 indexed
        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next

        lindex = k - 1
        rindex = len(arr) - k
        arr[lindex],arr[rindex] = arr[rindex],arr[lindex]
        cur = ListNode()
        temp = cur
        for i in arr:
            temp.next = ListNode()
            temp = temp.next
        return cur.next   