def copyList(head: Node) -> Node

    oldToCopy = {}
    curr = head
    
    while head:
        copy = Node(curr.val)
        oldToCopy[curr] = copy
        curr = curr.next
        
    curr = head
    while curr:
        copy = oldToCopy[curr]
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        curr = curr.next
        
    return oldToCopy[head]