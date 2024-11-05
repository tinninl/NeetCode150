def maxArea(self, height: List[int]) -> int:
    
    l, r = 0, len(height) - 1
    
    w, h, a = 0, 0, 0 # width, height, area
    
    maxArea = 0
    
    while l < r:
        
        # Calculate area
        w = r - l
        h = min(height[l], height[r])
        area = h * w
        
        # Check and update maxArea
        maxArea = max(area, maxArea)
        
        # Update pointers
        if (height[l] < height[r]):
            l += 1
            
        else:
            r -= 1
            
    return maxArea