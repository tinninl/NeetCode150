def longest(s: str, k: int) -> int:
    
    l, r = 0, 0 # start and ending indices of window
    
    maxFreq = 0
    maxLength = 0
    
    count = {} # key = char, value = freq
    
    for r in range(len(s)):
        
        count[s[r]] = 1 + count.get(s[r], 0) # Add to window
        maxFreq = max(maxFreq, count[s[r]]) # Update maxFreq
        
        while ((r - 1 + 1) - maxFreq) > k:  # If window is too big, remove elements from the left
            count[s[l]] -= 1
            l += 1
            
        maxLength = max(maxLength, r - l + 1) # r - l + 1 = length of window
         
    return maxLength
    