/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    // Current node is head 
    let node = head;
    // Initialize references to previous and next
    // These are equivalent to arrayList[i - 1] for prev
    //                      and arrayList[i + 1] for next
    let next = null;
    let prev = null;

    // While we're not at end of the list
    while(node) {
        // Our next reference is current node's next
        next = node.next;
        // Initially, assign next to be null, because our head is now
        // our tail. Otherwise, our next pointer should point
        // to our 'left', not 'right'
        node.next = prev;
        // Update our prev to be current node
        prev = node;
        // Update our node to the next node
        node = next;
    }
    // Return the new head, which was our tail
    return prev;

};