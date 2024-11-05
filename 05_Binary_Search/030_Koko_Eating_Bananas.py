import math


def sol(piles: list[int], h: int) -> int:
    
    fastest = max(piles) # fastest eating speed
    slowest = 1
    
    minSpeed = fastest
    
    while slowest < fastest:
        
        mid = slowest + ((fastest - slowest) // 2)
        
        time = 0 # time to eat all piles
        
        for p in piles:
            time += math.ceil(float(p) / mid)
            
        if time <= h: # if time under h, found a possible solution
            minSpeed = mid      
            
        else: 
            slowest = mid + 1
    
    return minSpeed