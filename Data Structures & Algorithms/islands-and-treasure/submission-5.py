from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Rows = len(grid)
        Cols = len(grid[0])
        seen = set()
        queue = deque()
        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == 0:
                    queue.append([i,j])
                    seen.add((i,j))
        
        coordinates = (
            [0,1], [0,-1],
            [1,0], [-1,0]
        )

        while queue:
            r, c = queue.popleft()

            for dr, dc in coordinates:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= Rows or nc >= Cols or (nr,nc) in seen:
                    continue
                if grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append([nr,nc])
                    seen.add((nr,nc))


