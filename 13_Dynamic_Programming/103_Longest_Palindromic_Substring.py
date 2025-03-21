"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

"""
Step One: What is the subproblem?
'ababa' is a palindrome if 'bab' is a palindrome, s[i:j] depends on s[i+1:j-1]

Step Two: What is the state?
dp[i][j] = True means its a palindrome from i to j

Step Three: What is the recurrence relation?
dp[i][j] = s[i] == s[j] and dp[i-1][j+1]

Step Four:
One letter substrings are palindromes
Two letter substrings MAY be palindromes
"""
class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        
        if n <= 1:
            return s
        
        start = 0
        maxLength = 0
        
        for i in range(n):
            
            # Handle odd palidromes
            l, r = i, i 
            
            while ((l >= 0) and (r < n) and (s[l] == s[r])):
                length = r - l + 1
                if length > maxLength:
                    maxLength = length
                    start = l
                    
                l -= 1
                r += 1
                
            # Handle even palindromes (r = i + 1 is the only difference)
            l, r = i, i + 1
            
            while ((l >= 0) and (r < n) and (s[l] == s[r])):
                length = r - l + 1
                if length > maxLength:
                    maxLength = length
                    start = l
                    
                l -= 1
                r += 1
                
        return s[start: start + maxLength]
                    