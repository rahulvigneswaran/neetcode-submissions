class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        res_max = 0
        for R in range(0, len(s)):
            while L <= R and s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            res_max = max(res_max, R-L + 1)
        return res_max