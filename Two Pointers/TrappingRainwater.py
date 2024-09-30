def trap(height: list[int]) -> int:
    
    area, totalArea = 0, 0
    
    l, r = 0, len(height) - 1
    
    maxLeft, maxRight = 0, 0
    
    while (l <= r):
        
        if (maxLeft < maxRight):
            
            area = max(maxLeft - height[l], 0)
            
            maxLeft = max(maxLeft, height[l])
            
            l += 1
            
        else:
            
            area = max(maxRight - height[r], 0)
            
            maxRight = max(maxRight, height[r])
            
            r -= 1
            
        totalArea += area
        
    return totalArea