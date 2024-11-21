import math
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        minHeap = []
        
        for x, y in points:
            
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])
            
        heapq.heapify(minHeap)
        
        for _ in range(k):
            
            distance, x, y = heapq.heappop(minHeap)
            res.appnd([x, y])
            
        return res
            