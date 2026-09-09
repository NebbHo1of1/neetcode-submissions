class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        Rows = len(grid)
        Cols = len(grid[0])

        seen = set()

        def dfs(r, c, seen, count):
            

            if count == len(word):
                return True
            if r < 0 or c < 0 or r >= Rows or c >= Cols or (r,c) in seen or grid[r][c] != word[count]:
                return False

            seen.add((r, c))
            
            res = (dfs(r + 1, c, seen, count + 1) or 
            dfs(r - 1, c, seen, count + 1) or 
            dfs(r, c + 1, seen, count + 1) or 
            dfs(r, c - 1, seen, count + 1))
            
            seen.remove((r,c))

            return res
        
        for i in range(Rows):
            for j in range(Cols):
                if dfs(i,j, seen, 0):
                    return True
        return False 