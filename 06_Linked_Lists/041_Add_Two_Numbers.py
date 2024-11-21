def add(h1: ListNode, h2: ListNode) -> int:
    
    # Extract the two numbers from the two lists
    num1 = 0   
    num2 = 0
    
    i = 0
    while h1:
        num1 += h1.val * pow(10, i)
        i += 1
        h1 = h1.next
        
    i = 0
    while h2:
        num2 += h2.val * pow(10, i)
        i += 1
        h2 = h2.next
    
    # Calculate sum    
    num3 = num1 + num2
    
    # Create a new list from sum
    dummy = ListNode()
    curr = dummy
    
    if num3 == 0:
        node = ListNode(0)
        return node
    
    while num3 > 0:
        
        digit = num3 % 10
        newNode = ListNode(digit)
        
        curr.next = newNode
        curr = newNode
        
        num3 = num3 // 10
        
    return dummy.next