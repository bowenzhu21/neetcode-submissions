class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            n = len(s)
            res = res + str(len(s)) + '#' + s

        return res
        #12#qwertyuiopas3#abc

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0

        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            n = int(s[l:r])
            res.append(s[r+1:r+n+1])
            l = r+n+1
        
        return res
