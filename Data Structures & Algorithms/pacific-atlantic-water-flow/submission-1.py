class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        ROWS = len(heights)
        COLS = len(heights[0])


        def helper(R, C, visited, prev):
            if (not(0<=R<ROWS) or 
                not(0<=C<COLS) or 
                (R, C) in visited or 
                heights[R][C] < prev): 
                return

            visited.add((R, C))

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in dirs:
                helper(R + dr, C + dc, visited, heights[R][C])

        for R in range(ROWS):
            helper(R, 0, pacific, float("-inf"))
            helper(R, COLS-1, atlantic, float("-inf"))
        
        for C in range(COLS):
            helper(0, C, pacific, float("-inf"))
            helper(ROWS-1, C, atlantic, float("-inf"))

        res = []

        for i in pacific:
            if i in atlantic:
                res.append(i)
        return res

        # O(N^2), O(N^2)
