"""
62. Unique Paths
There is a robot on an m x n grid. 
The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that 
the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:

1 <= m, n <= 100
"""

"""
Step One: What is the subproblem?
The num of paths to reach a cell depends on the cells above and to the left of it

Step Two: What is the state?
Let dp[i][j] = the num of paths it takes from i,j to m-1,n-1

Step Three: What is the recurrence relation?
dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

Step Four: Base Case(s):
dp[m-1][n-1] = 0
The cells on the bottom row and rightmost col have only 1 path to the end
"""
class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:

        # Initialize a matrix of dimensions m * n
        matrix = [[0] * n for _ in range(m)] 

        # Set rightmost column to 1s
        for i in range(n):
            matrix[-1][i] = 1

        # Set bottom row to 1s
        for i in range(m):
            matrix[i][-1] = 1
        
        # Fill the rest of the matrix
        for i in range(m - 2, -1, -1):  # Start from second last row upwards
            for j in range(n - 2, -1, -1):  # Start from second last column leftwards
                matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
                
        return matrix[0][0]
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        ROWS = m
        COLS = n
        memo = {}
        
        def dfs(r, c):
            
            # Check bounds
            if (r == ROWS - 1) or (c == COLS - 1):
                return 1
            
            # Return cached result
            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            
            return memo[(r, c)]

        return dfs(0, 0)
"""
The trick is to realize that the bottom row and rightmost col cells have only one path
The other cells are the sums of the right and bottom adj cells
"""
        
            