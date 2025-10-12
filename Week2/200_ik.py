from typing import List


class Solution:

    # DFS
    # Time: O(nm)
    # Space: O(nm)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= row:
                return
            if j < 0 or j >= col:
                return
            if (i, j) in visited:
                return
            if grid[i][j] == '0':
                return

            visited.add((i, j))

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i, j) not in visited:
                    cnt += 1
                    dfs(i, j)
        return cnt


