def isValid(s: str) -> bool:
    
    stack = []
    
    map = { ")" : "(", "]" : "[", "}" : "{" }
    
    for b in s:
            
        if b in map:
            
            if stack and stack[-1] == map.get(b):
                stack.pop()
                
            else:
                return False
            
        else:
            stack.append(b)
        
    if stack:
        return False
    else:
        return True
    