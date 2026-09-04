class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])

        maxArea = 0
        seen = set()

        def dfs(r, c, seen):
            area = 1
            if r < 0 or c < 0 or r >= Rows or c >= Cols or (r,c) in seen or grid[r][c] == 0:
                return 0
            
            seen.add((r,c))
            area += dfs(r + 1, c, seen)
            area += dfs(r - 1, c, seen)
            area += dfs(r, c + 1, seen)
            area += dfs(r, c - 1, seen)

            return area
        
        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == 1 and (i,j) not in seen:
                    maxArea = max(maxArea, dfs(i, j, seen))
        return maxArea
        


            
