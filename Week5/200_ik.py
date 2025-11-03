from typing import List


class Solution:
    # BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            queue = [(i, j)]
            while queue:
                x, y = queue.pop(0)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < len(grid)
                        and 0 <= ny < len(grid[0])
                        and grid[nx][ny] == "1"
                    ):
                        grid[nx][ny] = "0"
                        queue.append((nx, ny))

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    bfs(i, j)
        return cnt


    # DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return
            if j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        return cnt

