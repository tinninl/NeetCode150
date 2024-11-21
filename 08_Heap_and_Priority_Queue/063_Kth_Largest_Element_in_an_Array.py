import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-n for n in nums]
        heapq.heapify(nums)

        for _ in range(k):
            x = heapq.heappop(nums)

        return -x
    
        # or use nthlargest, py function that returns heap of largest elements of size k
        # return heapq.nlargest(k,nums)[-1]