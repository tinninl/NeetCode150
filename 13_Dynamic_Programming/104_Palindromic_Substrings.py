def countPalindromes(s: str) -> int:
    
    n = len(s)
    
    if n <= 1:
        return n
    
    res = 0
    
    def isPali(l, r):
        
        while l < r:
            
            if s[l] != s[r]:
                return False
            
            else:
                l += 1
                r -= 1
                
        return True
    
    for i in range(n):
        
        for j in range(i, n):
            
            if isPali(i, j):
                res += 1
        
    return res