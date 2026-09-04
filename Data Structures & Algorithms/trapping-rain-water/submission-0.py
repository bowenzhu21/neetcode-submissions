class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        res = 0

        #[0,2,0,3,1,0,1,3,2,1]
        # l = 0, lmax = 0, r = 9, rmax = 1, h[l] = 0, h[r] = 1, res = 0
        # l = 1, lmax = 2, r = 9, rmax = 1, h[l] = 2, h[r] = 1, res = 0
        # l = 1, lmax = 2, r = 8, rmax = 2, h[l] = 2, h[r] = 2, res = 0
        # l = 2, lmax = 2, r = 8, rmax = 2, h[l] = 0, h[r] = 2, res = 2
        # l = 3, lmax = 3, r = 8, rmax = 2, h[l] = 3, h[r] = 2, res = 2
        # l = 3, lmax = 3, r = 7, rmax = 3, h[l] = 3, h[r] = 3, res = 2
        # l = 4, lmax = 3, r = 7, rmax = 2, h[l] = 1, h[r] = 2, res = 4
        # l = 5, lmax = 3, r = 7, rmax = 2, h[l] = 0, h[r] = 2, res = 7
        # l = 6, lmax = 3, r = 7, rmax = 2, h[l] = 1, h[r] = 2, res = 9

        while l < r:
            if lmax <= rmax:
                l += 1
                n = height[l]
                if n < lmax and n < rmax:
                    res += min(lmax,rmax) - n
                lmax = max(lmax, n)
            else:
                r -= 1
                n = height[r]
                if n < lmax and n < rmax:
                    res += min(lmax,rmax) - n
                rmax = max(rmax, n)
        
        return res