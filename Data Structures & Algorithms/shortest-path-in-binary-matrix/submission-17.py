from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        seen = {(0,0)}
        count = 1
        queue = deque([(0,0,count)])

        if grid[0][0] == 1:
            return -1

        directions = [
            (-1, 0), (1, 0), 
            (0, -1), (0, 1),  
            (-1, -1), (-1, 1), 
            (1, -1), (1, 1)
            ]

        while queue:
            r, c, count = queue.popleft()

            if (r,c) == (Rows - 1, Cols - 1):
                return count

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nc < 0 or nr >= Rows or nc >= Cols or (nr,nc) in seen or grid[nr][nc] == 1:
                    continue 
                
                seen.add((nr,nc))
                queue.append((nr,nc, count + 1))
        return -1