def solution(root: TreeNode, k: int) -> int:
    
    n = 0 
    curr = root
    stack = []
    
    while curr and stack:
        
        while curr:
            
            stack.append(curr)
            curr = curr.left
            
        curr = stack.pop()
        n += 1
        
        if n == k:
            return curr.val
        
        curr = curr.right
        
    return -1