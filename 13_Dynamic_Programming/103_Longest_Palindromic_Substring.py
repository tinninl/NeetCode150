def longestPalindrome(s: str) -> str:
    
    n = len(s)
    
    if n <= 1:
        return s

    longest = 0
    start = 0
    length = 0
    
    for m in range(n):
        
        length = 1
        
        l = m - 1      
        r = m + 1        
           
        while l >= 0 and s[l] == s[m]:
            length += 1
            l -= 1
                 
        while r < n and s[r] == s[m]:
            length += 1
            r += 1
        
        while (l >= 0) and (r < n) and s[l] == s[r]:
                
                length += 2
                l -= 1
                r += 1
        
        if length > longest:
            longest = length
            start = l + 1

    
    print('start = ', start)
    print('longest = ', longest)
    return s[start: start + longest]
        
s = 'babad'
                
print(longestPalindrome(s))