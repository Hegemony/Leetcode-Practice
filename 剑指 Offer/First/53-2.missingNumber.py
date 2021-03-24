class Solution:
    def missingNumber(self, nums) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == mid:
                i = mid + 1
            else:
                j = mid - 1
        return i