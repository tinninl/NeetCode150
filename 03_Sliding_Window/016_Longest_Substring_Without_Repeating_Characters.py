def sub(s: str) -> int:

    charSet = set()
    
    length, maxLength = 0, 0
    
    l = 0
    r = 0
    
    for r in range(len(s)):
        
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
            
        charSet.add(s[r])
        length = r - l + 1
        maxLength = max(maxLength, length)
        
    return maxLength
    
s = 'abafcdabce'
print(sub(s))