class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1

            if cnt > mid:
                right = mid
            else:
                left = mid + 1
            print(mid, left, right)
        return left


print(Solution().findDuplicate([1, 3, 4, 2, 2]))
