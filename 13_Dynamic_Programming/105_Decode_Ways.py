class Solution:
    def decode(self, s: str) -> int:

        n = len(s)

        # Cache[i] represents the number of decodings for a string of length i
        cache = [0] * (n + 1)

        cache[0] = 1 # Only one way to decode an empty string

        # Edge Case: First letter is a 0  
        if s[0] == '0':
            cache[1] = 0      
        else:
            cache[1] = 1

        for i in range(2, n):

            # Decode as a single digit number
            if s[i - 1] != '0':
                cache[i] += cache[i - 1]

            # Decode as a double digit number (10 - 19, 20 - 26)  
            if (s[i - 2] == '1') or (s[i - 2] == '2' and s[i - 1] <= '6'):
                cache[i] += cache[i - 2]

        return cache[n]