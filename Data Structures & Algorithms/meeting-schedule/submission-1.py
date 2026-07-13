"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        p1 = 0
        while p1<len(intervals)-1:
            #the idea is that we take the end and see if it is greater than the start
            if intervals[p1].end > intervals[p1+1].start:
                return False

            p1 += 1

        return True

