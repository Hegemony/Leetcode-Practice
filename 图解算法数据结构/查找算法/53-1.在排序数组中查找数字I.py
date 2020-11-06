class Solution:
    def search(self, nums, target: int) -> int:
        self.cnt = 0

        def binary_search(l, r, nums, target):
            if l <= r:
                print(l, r)
                mid = (l + r) // 2
                if nums[mid] == target:
                    self.cnt += 1
                    binary_search(l, mid - 1, nums, target)
                    binary_search(mid + 1, r, nums, target)
                elif nums[mid] < target:
                    l = mid + 1
                    binary_search(l, r, nums, target)
                else:
                    r = mid - 1
                    binary_search(l, r, nums, target)

        binary_search(0, len(nums) - 1, nums, target)
        return self.cnt


print(Solution().search([5, 7, 7, 8, 8, 10], 8))



class Solution1:
    def search(self, nums: [int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i
        return helper(target) - helper(target - 1)
