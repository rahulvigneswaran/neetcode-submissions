class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0 
        R = len(heights) - 1

        res_max = 0
        while L < R:
            res_max = max(res_max, min(heights[L], heights[R])*(R-L))
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return res_max