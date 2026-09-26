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
        for interval in intervals:
            while rooms and rooms[0]<=interval.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms,interval.end)
            room = max(room, len(rooms))
        return room