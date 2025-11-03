class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        last = None
        for interval in intervals:
            if last:
                if last[1] > interval[0]:
                    return False
            last = interval
        return True
