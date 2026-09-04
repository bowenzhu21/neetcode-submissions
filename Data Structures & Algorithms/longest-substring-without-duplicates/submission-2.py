class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        seen = set()
        l, r = 0, 1
        res = 0
        seen.add(s[l])

        # abcabcbb
        # l = 0, r = 1, s[l] = a, s[r] = b, seen = (a,b), res = 2
        # l = 0, r = 2, s[l] = a, s[r] = c, seen = (a,b,c), res = 3
        # l = 0, r = 3, s[l] = a, s[r] = a, seen = (a,b,c), res = 3
            # l = 1, r = 3, s[l] = b, s[r] = a, seen = (b,c,a), res = 3
        # l = 1, r = 4, s[l] = b, s[r] = b, seen = (b,c,a), res = 3
            # l = 2, r = 4, s[l] = c, s[r] = b, seen = (c,a,b), res = 3
        # l = 2, r = 5, s[l] = c, s[r] = c, seen = (c,a,b), res = 3
            # l = 3, r = 5, s[l] = a, s[r] = c, seen = (a,b,c), res = 3

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        
        return res