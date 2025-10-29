def merge(h1: Optional[ListNode], h2: Optional[ListNode]) -> ListNode:
    
    newHead = None
    
    # if one of the lists are empty, simply return the head of the other one
    if not h2:
        return h1
    elif not h1:
        return h2
    
    # Determine the head of the merged list
    if h1.val <= h2.val:
        newHead = h1
        h1 = h1.next
    else:
        newHead = h2
        h2 = h2.next
     
    # Add the remaining elements
    curr = newHead
        
    while h1 and h2:
        
        if h1.val <= h2.val:
            curr.next = h1
            h1 = h1.next
        
        else:
            curr.next = h2
            h2 = h2.next
            
        curr = curr.next
        
    # If we reach the end of one list, tack on the other one     
    if not h1:
        curr.next = h2
        
    elif not h2:
        curr.next = h1
    
    return newHead
        
    
        