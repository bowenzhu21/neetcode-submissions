class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c not in valid:
                stack.append(c)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if valid[c] != prev:
                    return False
        
        if not stack:
            return True
        else:
            return False