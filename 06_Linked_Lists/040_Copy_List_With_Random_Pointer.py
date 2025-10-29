# Due to the random pointers, 
# we need to have copies of every node before building a new list

# Therefore, two iterations are needed
# One to make copies
# The second to build the list

def copyList(head: Node) -> Node:

    # Store copies of every node in a hashmap
    
    oldToCopy = {} # {original: copy}
    
    curr = head   
    while head:
        copy = Node(curr.val)
        oldToCopy[curr] = copy
        curr = curr.next
        
    
    # Construct a new list using the copies
    
    curr = head
    while curr:
        copy = oldToCopy[curr]
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        curr = curr.next
    
    # Return copy of head
    return oldToCopy[head]