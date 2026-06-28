import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        q = list(set((nums.count(i), i) for i in nums))
        heapq.heapify(q)
        while len(q) > k:
            heapq.heappop(q)
        return [i for j,i in q]