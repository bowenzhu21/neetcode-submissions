class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        nulls = 0

        for n in nums:
            if n != 0:
                total = total*n
            else:
                nulls += 1
        
        res = []
        for n in nums:
            if nulls >= 2 or nulls == 1 and n != 0:
                res.append(0)
            elif n == 0:
                res.append(total)
            else:
                res.append(total//n)
        
        return res
