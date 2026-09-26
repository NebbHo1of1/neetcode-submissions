from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        count = 0
        seen = set()
        queue = deque()

        directions = [
            (1,0), (-1,0), 
            (0,1), (0,-1)
        ]
        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == "1" and (i,j)not in seen:
                    seen.add((i,j))
                    queue.append((i,j))
                    count += 1

                    while queue:
                        r, c = queue.popleft()
                        
                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc

                            if nr < 0 or nc < 0 or nr >= Rows or nc >= Cols or (nr,nc) in seen or grid[nr][nc] == "0":
                                continue
                            seen.add((nr,nc))
                            queue.append((nr,nc))                  
        return count





        
