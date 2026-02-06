
def isValidPalindrome(s: str) -> bool:

    l, r = 0, len(s) - 1
    
    while l < r:
        
        if not s[l].isalnum(): # check if not alpha-numeric characters
            l += 1
            
        elif not s[r].isalnum():
            r -= 1
            
        else:
            
            if (s[l].lower() != s[r].lower()):
                return False
        
            l += 1
            r -= 1
        
        return True
   
s = 'race car'
print(isValidPalindrome(s))         
