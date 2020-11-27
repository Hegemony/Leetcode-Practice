class Solution:
    def maxProduct(self, nums):
        res = float("-inf")
        imax, imin = 1, 1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            res = max(res, imax)
        return res


# print(Solution().maxProduct([2, 3, -2, 4]))


class Solution1:
    def maxProduct(self, nums) -> int:
        dp_max = [0 for i in range(len(nums))]
        dp_min = [0 for i in range(len(nums))]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])  # 整数的情况要一直乘下去，包括负负得正的情况
            dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i], dp_max[i - 1] * nums[i])  # 负数的情况要保留最小的（也就是负数的最大）
        return max(max(dp_max), max(dp_min))


print(Solution1().maxProduct([2, 3, -2, 4]))
