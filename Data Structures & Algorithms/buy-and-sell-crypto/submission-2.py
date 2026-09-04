class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        r = 1

        #[5,1,5,6,7,1,10]
        # l = 0, p[l] = 5, r = 1, p[r] = 1, res = 0
        # l = 1, p[l] = 1, r = 2, p[r] = 5, res = 4
        # l = 1, p[l] = 1, r = 3, p[r] = 6, res = 5
        # l = 1, p[l] = 1, r = 4, p[r] = 7, res = 6
        # l = 1, p[l] = 1, r = 5, p[r] = 1, res = 6


        while r < len(prices):
            res = max(prices[r] - prices[l], res)
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                r += 1
        
        return res