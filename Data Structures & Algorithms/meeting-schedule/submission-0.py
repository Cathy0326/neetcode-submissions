"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])
        s,e = 1,0
        while s < len(intervals):
            if start[s] <= end[e]:
                return False
            return True 
