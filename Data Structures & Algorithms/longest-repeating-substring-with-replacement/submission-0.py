class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #AAABABB, k = 1, len - max <= k
        # A     , A:1       , max = 1, len = 1, len - max = 0
        # AA    , A:2       , max = 2, len = 2, len - max = 0
        # AAA   , A:3       , max = 3, len = 3, len - max = 0
        # AAAB  , A:3, B:1  , max = 3, len = 4, len - max = 1
        # AAABA , A:4, B:1  , max = 4, len = 5, len - max = 1
        # AAABAB, A:4, B:2  , max = 4, len = 6, len - max = 2
            # AABAB, A:3, B:2   , max = 3, len = 5, len - max = 2
            # ABAB, A:2, B:2    , max = 2, len = 4, len - max = 2
            # BAB, A:1, B:2     , max = 2, len = 3, len - max = 1
        # BABB, A:1, B:3    , max = 3, len = 4, len - max = 1

        window = {}
        most = 0
        res = 0
        l = 0

        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            most = max(most, window[c])
            while (r - l + 1 - most) > k:
                window[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res