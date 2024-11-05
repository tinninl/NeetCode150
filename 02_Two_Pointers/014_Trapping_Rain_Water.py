def trap(height: list[int]) -> int:
    
    area, totalArea = 0, 0
    
    l, r = 0, len(height) - 1
    
    maxLeft, maxRight = 0, 0
    
    while (l <= r):
        
        if (maxLeft < maxRight):
            
            area = maxLeft - height[l]
            
            maxLeft = max(maxLeft, height[l])
            
            l += 1
            
        else:
            
            area = maxRight - height[r]
            
            maxRight = max(maxRight, height[r])
            
            r -= 1
            
        if area > 0:
            totalArea += area
        
    return totalArea