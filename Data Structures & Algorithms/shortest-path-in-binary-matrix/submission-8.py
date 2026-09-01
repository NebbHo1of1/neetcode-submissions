from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        if grid[0][0] == 1 or grid[Rows-1][Cols-1] == 1:
            return -1
        seen = set()
        seen.add((0,0))
        queue = deque([(0,0,1)])

        coordinates = (
            [0,1], [0,-1], 
            [1,0], [-1,0], 
            [1,1], [1,-1], 
            [-1,1], [-1,-1]
        )

        while queue:
            r, c, length = queue.popleft()
            if r == Rows - 1 and c == Cols - 1:
                return length

            for dr, dc in coordinates:
                nr = dr + r
                nc = dc + c

                if nr >= Rows or nc >= Cols or nr < 0 or nc < 0 or (nr,nc) in seen or grid[nr][nc] == 1:
                    continue

                queue.append((nr,nc,length + 1))
                seen.add((nr,nc))
        return -1