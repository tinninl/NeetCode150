def remove(head: ListNode, n: int) -> None:
    
    if not head or not head.next: # In case list has exactly one element
        return None
    
    left = head
    right = head
    
    while n > 0 and right: # question says n always <= num of nodes, can never go out of bounds
        right = right.next
        n -= 1
        
    while right.next:
        left = left.next
        right = right.next
        
    left.next = left.next.next
    
    return head