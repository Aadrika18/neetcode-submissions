class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        numsc = [-n for n in nums]
        
        heapq.heapify(numsc)
        while k > 0:
            k -= 1
            popped = heapq.heappop(numsc)
        
        return -popped
            
        