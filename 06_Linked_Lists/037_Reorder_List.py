def reorder(head: ListNode) -> None:
    
    # Find the middle of the list
    
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    mid = slow
    
    # Reverse the second half of the list, starting from mid
    
    prev = None
    while mid:
        temp = mid.next
        mid.next = prev
        prev = mid
        mid = temp
        
    # Now prev is the head of the reversed list
    
    # Merge both lists
    l1 = head
    l2 = prev
    
    while l2.next:
        
        temp1 = l1.next
        l1.next = l2
        l1 = temp1
        
        temp2 = l2.next
        l2.next = temp1
        l2 = temp2
    
    
        