class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = ''
        
        for ch in s:
            if ch.isalnum():
                snew += ch.lower()
        
        l = 0
        r = len(snew) - 1

        while l < r:
            if snew[l] != snew[r]:
                return False
            l += 1
            r -= 1
        
        return True