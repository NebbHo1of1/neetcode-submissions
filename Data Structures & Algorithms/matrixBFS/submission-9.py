from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        seen = set()
        seen.add((0,0))
        queue = deque([(0,0,0)])
        directions = (
                [0,1], [0,-1],
                [1,0], [-1,0]
            )
        if grid[0][0] == 1:
            return -1
        while queue:
                r, c, length = queue.popleft()

                if r == Rows - 1 and c == Cols - 1:
                    return length
            
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nc < 0 or nr >= Rows or nc >= Cols or (nr,nc) in seen or grid[nr][nc] == 1:
                        continue

                    queue.append((nr,nc,length + 1))
                    seen.add((nr,nc))
        return -1  


        