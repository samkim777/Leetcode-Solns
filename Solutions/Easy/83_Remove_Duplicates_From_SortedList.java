_/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        // If empty, return empty
        // Should end when at end of list, when next refers to null
        // If first node equal to second, 
            // Delete second node by having first node's next reference
                // the node after 2nd, so third node
        // Else keep iterating  
        ListNode cur = head;
        if (head == null) return head;
        while(cur.next != null) {
            if (cur.val == cur.next.val) cur.next = cur.next.next;
            else cur = cur.next;
        } 
        return head;       
    }
}