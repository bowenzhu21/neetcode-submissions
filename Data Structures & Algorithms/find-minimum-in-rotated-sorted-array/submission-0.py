class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # 3,4,5,6,1,2

        # 6,1,2,3,4,5
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                #rotation on the right
                l = m + 1
            else:
                #rotation on the left
                r = m

        return nums[l]