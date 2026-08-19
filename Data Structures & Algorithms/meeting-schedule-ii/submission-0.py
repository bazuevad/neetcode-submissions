"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        room = 0
        intervals.sort(key=lambda i: i.start)
        for i in intervals:
            start = i.start
            end = i.end
            if rooms and rooms[0]<=start:
                heapq.heappop(rooms)
            heapq.heappush(rooms,end)
            room = max(room,len(rooms))
        return room