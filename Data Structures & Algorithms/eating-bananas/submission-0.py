class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo,hi = 1, max(piles)
        res = hi
        while lo<=hi:
            k = (lo+hi)//2
            totalTime = 0
            for p in piles:
                totalTime+=math.ceil(float(p)/k)
            if totalTime<=h:
                res = k
                hi = k-1
            else:
                lo=k+1
        return res

