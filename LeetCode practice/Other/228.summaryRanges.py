class Solution:
    def summaryRanges(self, nums):
        n = len(nums)
        # 初始化双指针均指向数组头部
        left = 0
        right = 0

        ans = []
        # 开始遍历
        while right < n:
            # 数组有序
            # 先限定边界，查找间隔大于 1 的部分
            while right < n - 1 and nums[right] + 1 == nums[right + 1]:
                right += 1
            # 找到间隔之后，将前面连续部分按照规定格式添加到结果列表中
            tmp = [str(nums[left])]
            if nums[left] != nums[right]:
                tmp.append('->')
                tmp.append(str(nums[right]))
            ans.append(''.join(tmp))
            # 维护更新 right 和 left
            right += 1
            left = right

        return ans