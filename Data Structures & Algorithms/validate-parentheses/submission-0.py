class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {']':'[', '}':'{', ')':'('}
        stack = []

        for ch in s:
            if ch in pairs:
                if not stack:
                    return False
                
                ob = stack.pop()
                if ob != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        
        if stack:
            return False
        
        return True