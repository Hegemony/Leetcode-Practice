"""
暴力枚举：超时
"""

class Solution:
    def findContinuousSequence(self, target: int):
        i = 1
        nums = []
        result = []
        while i < target:
            nums.append(i)
            i += 1

        for i in range(len(nums) // 2):
            for j in range(i, len(nums)):
                res = nums[i:j]
                if sum(res) == target:
                    result.append(res)
        return result

print(Solution().findContinuousSequence(15))

"""
利用滑动窗口的思想，
通过双指针实现滑动窗口

1.当窗口的和小于 target 的时候，窗口的和需要增加，所以要扩大窗口，窗口的右边界向右移动；
2.当窗口的和大于 target 的时候，窗口的和需要减少，所以要缩小窗口，窗口的左边界向右移动；

3.当窗口的和恰好等于 target 的时候，我们需要记录此时的结果。设此时的窗口为 [i, j)，
那么我们已经找到了一个 i开头的序列，也是唯一一个 i开头的序列，接下来需要找 i+1 开头的序列，所以窗口的左边界要向右移动。
"""

class Solution:
    def findContinuousSequence(self, target: int):
        i = 1
        j = 1
        sum = 0
        result = []
        while i <= target // 2:
            if sum < target:
                sum += j
                j += 1
            elif sum > target:
                sum -= i
                i += 1
            else:
                res = list(range(i, j))
                result.append(res)
                sum -= i
                i += 1
        return result