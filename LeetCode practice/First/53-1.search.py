class Solution:
    def search(self, nums, target: int) -> int:
        l = len(nums)
        if l == 0:
            return 0
        left_position = self.findLeftPosition(nums, l, target)
        right_position = self.findRightPosition(nums, l, target)
        print(left_position, right_position)
        return right_position - left_position

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
        return i

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
        return i


print(Solution().search([5, 7, 7, 8, 8, 10], 8))
