"""
Nearly identical to Longest Palindromic Substring, in fact its easier.
Instead of tracking starting index and length of longest pali,
just track number of palis. Only changes made are to return stmnt and tracking variables.
"""
class Solution:
    
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        
        if n <= 1:
            return s
        
        res = 0
        
        for i in range(n):
            
            # Handle odd palidromes
            l, r = i, i 
            
            while ((l >= 0) and (r < n) and (s[l] == s[r])):
                
                res += 1
                l -= 1
                r += 1
                
            # Handle even palindromes (r = i + 1 is the only difference)
            l, r = i, i + 1
            
            while ((l >= 0) and (r < n) and (s[l] == s[r])):
              
                res += 1   
                l -= 1
                r += 1
                
        return res