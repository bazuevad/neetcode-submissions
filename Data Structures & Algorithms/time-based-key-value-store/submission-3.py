from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        pairs = self.map[key]
        lo,hi = 0, len(pairs)-1
        prev = None
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if pairs[mid][0]<=timestamp:
                prev = mid
                lo = mid+1
            else:
                hi = mid-1
        if prev is None:
            return ""
        return pairs[prev][1]
