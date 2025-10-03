from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        
        def paint(i,j):
            dirs = [(-1,0),(0,-1),(0,1),(1,0)]
            queue = [(i,j)]
            
            while queue:
                cur_x,cur_y = queue.pop(0)
                grid[cur_x][cur_y] = '0'
                
                for move_x,move_y in dirs:
                    if 0<=cur_x+move_x<n_rows and 0<=cur_y+move_y<n_cols:
                        if grid[cur_x+move_x][cur_y+move_y] == '1':
                            queue.append((cur_x+move_x,cur_y+move_y))
                            grid[cur_x+move_x][cur_y+move_y] = '0'
         
        num_islands = 0
        
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == '1':
                    paint(i,j)
                    num_islands+=1
        return num_islands
    
s = Solution().numIslands(grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(s)

s = Solution().numIslands(grid=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
print(s)