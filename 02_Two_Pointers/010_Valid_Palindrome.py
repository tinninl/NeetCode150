"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters
"""
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
