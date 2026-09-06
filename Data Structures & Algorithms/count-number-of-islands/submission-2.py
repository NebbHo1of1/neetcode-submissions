class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        count = 0
        seen = set()
        def dfs(r, c, seen):
            if r < 0 or c < 0 or r >= Rows or c >= Cols or (r,c) in seen or grid[r][c] == "0":
                return
            
            seen.add((r,c))

            dfs(r + 1, c, seen)
            dfs(r - 1, c , seen)
            dfs(r, c + 1, seen)
            dfs(r, c - 1, seen) 
        
        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == "1" and (i,j) not in seen:
                    dfs(i,j,seen)
                    count += 1
        return count 