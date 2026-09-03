class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        res = 0

        for n in nums:
            l = 1
            if n - 1 not in nset:
                while n + l in nset:
                    l += 1
            res = max(l, res)
        
        return res
                