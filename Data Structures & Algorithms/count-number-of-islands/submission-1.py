class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def helper(R, C):
            if (not(0<=R<ROWS) or
                not(0<=C<COLS) or
                grid[R][C] == "0"):
                return
            
            grid[R][C] = "0"
            
            for dR, dC in dirs:
                helper(R + dR, C + dC)
            
        for R in range(ROWS):
            for C in range(COLS):
                if grid[R][C] == "1":
                    res += 1
                    helper(R, C)

        return res

        # O(N^2), O(N)
