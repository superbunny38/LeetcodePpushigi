from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited, n = set(),len(grid)
        dirs = [[-1,0],[0,-1],[1,0],[0,1]]
        
        def invalid(x,y):
            if x<0 or y<0 or x>=n or y>=n:
                return True
        
        def dfs(x,y):
            visited.add((x,y))
            for move_x,move_y in dirs:
                if invalid(x+move_x,y+move_y) or (x+move_x,y+move_y) in visited:
                    continue
                if grid[move_x+x][move_y+y]:
                    dfs(move_x+x,move_y+y)
        
        def bfs():
            ret, queue = 0, deque(visited)
            while queue:
                for i in range(len(queue)):
                    new_x,new_y = queue.popleft()
                    
                    for move_x,move_y in dirs:
                        if invalid(new_x+move_x,new_y+move_y) or (new_x+move_x,new_y+move_y) in visited:
                            continue
                        
                        if grid[new_x+move_x][new_y+move_y]:
                            return ret
                        queue.append((move_x+new_x,move_y+new_y))
                        visited.add((move_x+new_x,move_y+new_y))
                ret +=1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()

grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

s = Solution().shortestBridge(grid=grid)
print(s)

grid =[[0,1,0],[0,0,0],[0,0,1]]

s = Solution().shortestBridge(grid=grid)
print(s)