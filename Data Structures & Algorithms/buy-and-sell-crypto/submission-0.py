class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        peak = prices[-1]
        for i in range(len(prices)):
            n = prices[len(prices) - i - 1]
            peak = max(n, peak)
            res = max(peak - n, res)
        return res