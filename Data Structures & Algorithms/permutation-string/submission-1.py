class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        have = {}
        l = 0

        #lecabee, ab, need = {a:1, b:1}
        # l = 0, r = 0, have = {l:1}
        # l = 0, r = 1, have = {l:1, e:1}



        for r, c in enumerate(s2):
            have[c] = have.get(c, 0) + 1
            if have == need:
                return True
            if r - l + 1 == len(s1):
                have[s2[l]] -= 1
                if have[s2[l]] == 0:
                    del have[s2[l]]
                l += 1
        
        return False