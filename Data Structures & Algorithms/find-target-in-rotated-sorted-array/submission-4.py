class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # [5,1,2,3,4], target = 1
        # l: {0:5} | r: {4:4} | m: {2:2}

        # l: {0:5} | r: {1:1} | m: {0:5}

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] > nums[r]:
                #rotate on the right
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                #rotate on the left
                if nums[m] < target <= nums[r]:
                    l = m + 1 
                else:
                    r = m - 1
        
        return -1
