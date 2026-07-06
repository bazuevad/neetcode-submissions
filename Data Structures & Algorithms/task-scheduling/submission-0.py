from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cool = deque()
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        time = 0

        while cool or heap:
            if cool and cool[0][1]==time:
                heapq.heappush(heap,cool.popleft()[0])
            
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt < 0:
                    cool.append((cnt, time + n + 1))

            time+=1

        return time

