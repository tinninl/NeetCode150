import heapq

def lastStoneWeight(self, stones: list[int]) -> int:
    
    stones = [-s for s in stones]
    
    heapq.heapify(stones)
    
    
    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        
        if second > first:
            heapq.heappush(stones, first - second)
    
    if not stones:
        return 0
    else:
        return stones[0] * -1