class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0 
        R = len(nums) - 1
        resMin = float("inf")
        while L <= R:
            if nums[L] < nums[R]:
                resMin = min(resMin, nums[L])
                return resMin
            m = L + (R - L) // 2
            resMin = min(resMin, nums[m])
            if nums[m] >= nums[L]: # Left side
                L = m + 1
            else: # Right side
                R = m - 1
        return resMin
