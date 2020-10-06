"""
错误解：
输入：
[1,3,2,2,2]
输出：
2
预期结果：
4
"""
class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        n = len(nums)
        numscopy = nums.copy()
        numscopy.sort()
        if nums == numscopy:
            print(nums, numscopy)
            return 0
        else:
            left = 0
            right = 0
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    left = i
                    break
            for m in range(n - 1, 0, -1):
                if nums[m] < nums[m - 1]:
                    right = m
                    break
            return (right - left + 1)

print(Solution().findUnsortedSubarray([1, 2, 3, 4, 5]))
print(Solution().findUnsortedSubarray([1, 2, 3, 4]))
print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

"""
用排序进行比对
"""
class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        n = len(nums)
        numscopy = nums.copy()
        numscopy.sort()
        if nums == numscopy:
            print(nums, numscopy)
            return 0
        else:
            left = 0
            right = 0
            for i in range(n):
                if nums[i] != numscopy[i]:
                    left = i
                    break
            for j in range(n-1, -1, -1):
                if nums[j] != numscopy[j]:
                    right = j
                    break
            return (right - left + 1)
