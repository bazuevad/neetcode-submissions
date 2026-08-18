import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dis = sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap,(dis,point))
        ret = []
        for _ in range(k):
            dis,point = heapq.heappop(heap)
            ret.append(point)
        return ret