class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])

        def dfs(r, c, seen):
            if r < 0 or c < 0 or r >= Rows or c >= Cols or (r,c) in seen or grid[r][c] == 1:
                return 0
            
            if r == Rows -1 and c == Cols -1:
                return 1
            
            seen.add((r,c))
            count = 0

            count += dfs(r + 1,c, seen)
            count += dfs(r - 1,c, seen)
            count += dfs(r,c + 1,seen)
            count += dfs(r,c - 1, seen)

            seen.remove((r,c))
            return count
        return dfs(0,0,set())



