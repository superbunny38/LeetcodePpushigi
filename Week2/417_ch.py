from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights),len(heights[0])
        direction = [[0,1],[1,0],[-1,0],[0,-1]]
        
        def dfs(visited, x, y):
            visited.add((x,y))
            orig_height = heights[x][y]
            for move_x, move_y in direction:
                cur_x,cur_y = x+move_x,y+move_y
                if 0<=cur_x<n and 0<=cur_y<m and orig_height<=heights[cur_x][cur_y] and (cur_x,cur_y) not in visited:
                    dfs(visited,cur_x,cur_y)
            return visited
        
        P, A = set(),set()
        for i in range(n):
            P = dfs(P,i,0)
        for j in range(m):
            P = dfs(P,0,j)
        for k in range(m):
            A = dfs(A,n-1,k)
        for o in range(n):
            A = dfs(A,o,m-1)
        return list(P&A)
                
        
        
s = Solution().pacificAtlantic(heights=[[1,1],[1,1],[1,1]])
print(s)