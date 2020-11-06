class Solution:
    def missingNumber(self, nums) -> int:
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return nums[-1] + 1
print(Solution().missingNumber([0, 1]))


class Solution1:
    def missingNumber(self, nums) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i

print(Solution1().missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8]))