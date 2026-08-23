class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            val = target - n
            if val in seen:
                return [seen[val], i]
            seen[n] = i