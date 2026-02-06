# Create a hashmap to store anagrams and their words
# Create buckets for each word to count the letters
# Convert the buckets into tuples, these will be the keys in our hashmap

from collections import defaultdict

class Solution:
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        anagrams = defaultdict(list)
        
        for s in strs:
            
            count = [0] * 26
            
            for c in s:
                
                count[ord(c) - ord('a')] += 1
            
                count = tuple(count)
                
            anagrams(count).append(s)
            
        return anagrams.values()
            