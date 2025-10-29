class ListNode:
    def _init_ (self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:        
    
    def reverseList(head:ListNode) -> ListNode:

        # Empty list
        if not head: 
            return None

        # Need to track previous and current nodes
        prev = None
        curr = head

        while curr:

            temp = curr.next # Also need a temp variable to help us swap references
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    
        # At the end of iterating, curr should point to null, prev should point to the tail

