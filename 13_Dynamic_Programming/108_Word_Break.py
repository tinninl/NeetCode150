"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

Example 1:

Input: s = "neetcode", wordDict = ["neet","code"]

Output: true
Explanation: Return true because "neetcode" can be split into "neet" and "code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen","ape"]

Output: true
Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.

Example 3:

Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

Output: false
Constraints:

1 <= s.length <= 200
1 <= wordDict.length <= 100
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
"""

"""
Step One: What is the subproblem?

Step Two: What is the state?
dp[i] = True means s[0:i] can be formed from the dict of words

Step Three: What is the recurrence relation?
dp[i] = True if dp[j] is True AND str[j:i] is also in the word dict (j < i)

Step Four: Base case(s)
dp[0] = True, an empty string
"""
class Solution:
    
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        wordSet = set(wordDict)      
        n = len(s)
        
        dp = [False] * (n + 1) # where dp[i] = a string of length i works
        
        dp[0] = True # an empty string will work
        
        for i in range(1, n + 1):
            
            for j in range(i):
                
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        
        return dp[n]

   