def hasCycle(head: ListNode) -> bool:
    
    # An empty list or a list with only one elem cant have a cycle
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False