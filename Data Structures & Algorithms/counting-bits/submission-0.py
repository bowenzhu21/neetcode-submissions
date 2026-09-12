class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(self.countOnes(i))
        return res
        
    def countOnes(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n = n // 2
        return count