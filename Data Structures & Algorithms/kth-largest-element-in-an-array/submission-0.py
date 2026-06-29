import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = nums[:]
        heapq.heapify(q)
        while q and len(q)>k:
            heapq.heappop(q)
        return heapq.heappop(q)
