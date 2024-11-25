import math


def sol(piles: list[int], h: int) -> int:
    
    # best case scenario is one banana
    # worst case scenario is the biggest pile
    max = max(piles)
    min = 1
    
    minSpeed = max
    
    while min < max:
        
        mid = (min + max) // 2
        
        time = 0 # time to eat all piles
        
        for p in piles:
            time += math.ceil(float(p) / mid)
            
        if time <= h: # if time under h, found a possible solution
            minSpeed = mid
            max = mid - 1      
        
        # If Koko cannot finish all piles, we need to check faster eating speeds  
        else: 
            min = mid + 1
    
    return minSpeed