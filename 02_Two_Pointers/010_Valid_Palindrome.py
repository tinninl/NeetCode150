def isValidPalindrome(s: str) -> bool:

    l, r = 0, len(str) - 1
    
    while l < r:
        
        while l < r and not str[l].isalnum(): # check if not alpha-numeric characters
            l += 1
            
        while r > 1 and not str[r].isalnum():
            r -= 1
            
        if (str[l].lower() != str[r].lower()):
            return False
        
        l += 1
        r -= 1
        
    return True
   
str = 'race car'
print(isValidPalindrome(str))         
