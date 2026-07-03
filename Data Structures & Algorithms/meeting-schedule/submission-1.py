"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda iv: iv.start)
        if len(intervals)<=1:
            return True
        curr = 1
        while curr < len(intervals):
            if intervals[curr].start<intervals[curr-1].end:
                return False
            curr +=1
        return True