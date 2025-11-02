from collections import defaultdict
from heapq import *
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]
        dist = {}

        while pq:
            time, node = heappop(pq)

            if node in dist:
                continue

            dist[node] = time

            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heappush(pq, (time + weight, neighbor))

        return max(dist.values()) if len(dist) == n else -1
