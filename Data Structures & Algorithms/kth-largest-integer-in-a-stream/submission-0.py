import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = nums[:]
        heapq.heapify(self.q)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        while self.q and len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]
