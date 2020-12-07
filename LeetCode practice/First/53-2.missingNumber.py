class Solution:
    def missingNumber(self, nums) -> int:
        i, j = 0, len(nums)
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == mid:
                i = mid + 1
            else:
                j = mid
        return i


class Solution1:
    def binarySearch(self, nums, target) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid
            else:
                return mid
        if i != len(nums) and nums[i] == target:
            return i
        return -1


print(Solution1().binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 9))


class Solution2:
    def searchRange(self, nums, target: int) -> int:
        l = len(nums)
        if l == 0:
            return [-1, -1]
        left_position = self.findLeftPosition(nums, l, target)
        if left_position == -1:
            return [-1, -1]
        right_position = self.findRightPosition(nums, l, target)
        print(left_position, right_position)
        return [left_position, right_position - 1]

    def findLeftPosition(self, nums, l, target):
        i, j = 0, l
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] == target:
                j = mid
            else:
                j = mid
            print(mid, i)
        if nums[i] == target:
            return i
        else:
            return -1

    def findRightPosition(self, nums, l, target):
        i, j = 0, l
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] == target:
                i = mid + 1
            else:
                j = mid
        if nums[i - 1] == target:
            return i
        else:
            return -1

# print(Solution2().searchRange([2, 2], 3))
