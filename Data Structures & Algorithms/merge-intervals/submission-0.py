class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted = intervals.sort()
        answ=[intervals[0]]
        for start,end in intervals[1:]:
            if start<=answ[-1][1]:
                answ[-1][1] = max(end,answ[-1][1])
            else:
                answ.append([start,end])
        return answ
