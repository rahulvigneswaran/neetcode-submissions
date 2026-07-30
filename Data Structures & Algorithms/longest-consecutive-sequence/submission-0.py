class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)

        res_max = 0
        for n in nums:
            res = 0
            if n-1 not in unique:
                while n in unique:
                    res += 1
                    n += 1
                    res_max = max(res_max, res)
        return res_max