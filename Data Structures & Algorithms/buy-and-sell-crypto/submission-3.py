class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res_max = 0

        L = 0
        R = L + 1

        while R < len(prices):
            res_max = max(res_max, prices[R] - prices[L])
            if prices[R] < prices[L]:
                L = R
                R = L + 1
            else:
                R += 1
        return res_max
            