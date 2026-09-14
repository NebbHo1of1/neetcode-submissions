from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        seen = set()
        queue = deque()

        coordinates = (
            [0,1], [0,-1], 
            [1,0], [-1,0]
        )
        time = 0
        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == 2:
                    seen.add((i,j))
                    queue.append(([i,j, time]))

        while queue:
            r, c, time = queue.popleft()
            for dr, dc in coordinates:
                nr = dr + r
                nc = dc + c

                if nr >= Rows or nc >= Cols or nr < 0 or nc < 0 or (nr,nc) in seen:
                    continue
                
                if grid[nr][nc] == 1:
                    queue.append(([nr,nc,time + 1]))
                    seen.add((nr,nc))
                    grid[nr][nc] = 2

        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == 1:
                    return -1
        return time
            
            


        