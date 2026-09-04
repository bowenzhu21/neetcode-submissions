class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0

        #[1,7,2,5,4,7,3,6]
        # l = 0:1, r = 7:6, h = 1, res = 
        while l < r:
            h = min(heights[l], heights[r])
            res = max(res, h * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
        