"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days 
you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 
[73]
Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

def dailyTemp(temperatures: list[int]) -> list[int]:
    
    res = [0] * len(temperatures)
    
    stack = [] # stack of pairs [temp, index]
    
    for i, t in enumerate(temperatures): # index = day, t = temp
        
        while stack and t > stack[-1][0]: # stack[-1][0] = peek temp
            prevDay = stack.pop()[1] # get the day
            res[prevDay] = i - prevDay # store the difference in days
            
        stack.append([t, i])
        
    return res