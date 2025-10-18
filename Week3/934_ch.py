from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        n =len(grid)
        visited = [[0]*n for _ in range(n)]
        
        def dfs(grid, x,y):
            stack = [(x,y)]
            while stack:
                cur_x,cur_y = stack.pop()
                visited[cur_x][cur_y]
        
        def bfs(grid,x,y):
            queue = [(x,y)]
            while queue:
                cur_x,cur_y = queue.pop(0)
                for move_x,move_y in dirs:
                    new_x,new_y = move_x+cur_x, move_y+cur_y
                    
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    dfs(grid,i,j)
    
    
s = Solution().shortestBridge(grid=[[0,1],[1,0]])