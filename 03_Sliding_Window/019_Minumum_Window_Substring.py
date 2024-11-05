def minWindow(s: str, t: str) -> str:
    
    if len(t) == 0:
        return ""
    
    countT, window = {}, {}
    
    start, end = 0, 0
    
    # Initialize map containing characters in T key = char, val = freq
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
        
    matches = 0
    target = len(countT)
    l = 0
    resLen = 10000
    
    for r in range(len(s)):
        
        c = s[r]
        
        window[c] = 1 + window.get(c, 0)
        
        if c in countT and window[c] == countT[c]:
            matches += 1
            
        while matches == target:
            
            if (r - l + 1) < resLen:
                
                res = l, r
                print(start, end)
                resLen = r - l + 1
            
            window[s[l]] -= 1
            
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                matches -= 1               
            
            l += 1
            
        print(window)
    start, end = res       
    return s[start:end + 1] 
      
            
s ='abodecodebanc'
t = 'abc'
print(minWindow(s,t))