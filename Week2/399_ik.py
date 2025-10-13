from collections import defaultdict
from typing import List


class Solution:
    # Graph: DFS
    # V = 변수(노드) 개수, E = equations(간선) 개수, Q = queries 개수

    # 그래프 구성: O(E)
    # 각 쿼리당: O(V + E) - 최악의 경우 모든 노드/간선 탐색
    # 전체: O(E + Q*(V + E))
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        # Build
        for (dividened, divisor), value in zip(equations, values):
            graph[dividened][divisor] = value
            graph[divisor][dividened] = 1 / value

        # Find
        def find(start, end, visited):
            if start not in graph:
                return -1.0
            if end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = find(neighbor, end, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0

        return [find(start, end, set()) for start, end in queries]

    # Graph: BFS
    # V = 변수(노드) 개수, E = equations(간선) 개수, Q = queries 개수

    # 그래프 구성: O(E)
    # 각 쿼리당: O(V + E) - 최악의 경우 모든 노드/간선 탐색
    # 전체: O(E + Q*(V + E))
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        # Build
        for (divisor, dividened), value in zip(equations, values):
            graph[divisor][dividened] = value
            graph[dividened][divisor] = 1 / value

        def find(start, end):
            if start not in graph:
                return -1.0
            if end not in graph:
                return -1.0

            visited = {start}
            queue = [(start, 1.0)]

            while queue:
                node, weight = queue.pop(0)

                if node == end:
                    return weight
                for neighbor, value in graph[node].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, weight * value))
            return -1.0

        return [find(start, end) for start, end in queries]




