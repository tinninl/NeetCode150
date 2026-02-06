# Create two arrays to track the frequencies of characters in each string.
# If the two arrays are equal, they are anagrams.

class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:   
        
        # Check equal lengths
        if len(s) != len(t): 
            return False
        
        # Two arrays, to track the letters and their frequencies in each string
        countS = [0] * 26 
        countT = [0] * 26
        
        # Fill the arrays
        for i in range(len(s)):
            
            countS[ord(s[i]) - ord('a')] += 1 
            countT[ord(t[i]) - ord('a')] += 1
        
        # Check that both arrays are the same
        for i in range(len(countS)):
            
            if countS[i] != countT[i]:
                return False
    
        return True