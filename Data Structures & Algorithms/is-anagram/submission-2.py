class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = Counter(s)
        str2 = Counter(t)
        return str1 == str2
        