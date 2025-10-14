from heapq import *
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        heap = []
        heappush(heap, intervals[0][1])

        for interval in intervals[1:]:
            curr_start, curr_end = interval
            prev_end = heap[0]

            if curr_start >= prev_end:
                # Reuse curent
                heappop(heap)
            heappush(heap, curr_end)
        return len(heap)






