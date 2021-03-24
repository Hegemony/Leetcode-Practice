class Solution:
    def search(self, nums, target: int) -> int:
        self.l = len(nums)
        if self.l <= 0:
            return 0
        left_position = self.leftSearch(nums, target)
        right_position = self.rightSearch(nums, target)
        print(left_position, right_position)
        return right_position - left_position + 1

    def leftSearch(self, nums, target):
        i, j = 0, self.l
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid
            else:
                j = mid
        return i

    def rightSearch(self, nums, target):
        i, j = 0, self.l
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid
            else:
                i = mid + 1
        return i - 1


# print(Solution().search([2, 2], 3))
# print(Solution().search([5, 7, 7], 7))
# print(Solution().search([1], 1))
# print(Solution().search([5, 7, 7, 8, 8, 9], 8))


class Solution1:
    def search(self, nums, target) -> int:
        self.l = len(nums)
        if self.l <= 0:
            return 0
        left_position = self.leftSearch(nums, target)
        right_position = self.rightSearch(nums, target)
        print(left_position, right_position)
        if left_position == -1 and right_position == -1:
            return 0
        else:
            return right_position - left_position + 1

    def leftSearch(self, nums, target):
        i, j = 0, self.l - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                j = mid - 1
        if i >= self.l or nums[i] != target:
            return -1
        return i

    def rightSearch(self, nums, target):
        i, j = 0, self.l - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        if j < 0 or nums[j] != target:
            return -1
        return j


print(Solution1().search([5, 7, 8, 9], 6))
