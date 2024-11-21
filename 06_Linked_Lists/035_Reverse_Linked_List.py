class ListNode:
    def _init_ (self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseList(head:ListNode) -> ListNode:
    
    if not head: # empty list
        return None

    prev = None
    curr = head
    next
    
    while curr:
        
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    return prev
        
"""
A B C
curr = A prev = None next = B
A must point to null, B must point to A
curr must point to B
prev must point to A
"""
