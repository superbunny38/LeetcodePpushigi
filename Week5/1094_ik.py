from heapq import *
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []  # (end, capa)
        passengers = 0

        for capa, start, end in trips:
            while heap and heap[0][0] <= start:
                passengers -= heappop(heap)[1]

            passengers += capa

            if passengers > capacity:
                return False
            heappush(heap, (end, capa))

        return True
