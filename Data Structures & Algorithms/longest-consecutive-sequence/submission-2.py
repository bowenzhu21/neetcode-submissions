class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in nset:
                l = 0
                while n + l in nset:
                    l += 1
                res = max(l, res)
        
        return res
                