class Solution:
    def maxSlidingWindow(self, nums, k: int):
        i = 0
        n = len(nums)
        if n == 0:
            return []
        res = []
        while i < n - k + 1:
            res.append(max(nums[i:i + k]))
            i += 1
        return res

"""
1.初始化： 双端队列 deque ，结果列表 res ，数组长度 n ；
2.滑动窗口： 左边界范围 i∈[1−k,n+1−k] ，右边界范围 j∈[0,n−1] ；
            若 i>0 且 队首元素 deque[0] == 被删除元素 nums[i - 1]：则队首元素出队；
            删除 deque 内所有 < nums[j]<nums[j] 的元素，以保持 deque 递减；
            将 nums[j] 添加至 deque 尾部；
            若已形成窗口（即 i≥0 ）：将窗口最大值（即队首元素deque[0] ）添加至列表 res 。
3.返回值： 返回结果列表 res。
"""

class Solution1:
    def maxSlidingWindow(self, nums, k: int):
        deque = []
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 制定规则, 始终奉行在deque[0]存储最大值
            # 先看deque队首, i=0 时因前面无值没有值可以滑出（所以从i=1开始，此时num[0]就是滑出值）
            # 同时当nums[i-1]滑出窗口时, 即判定条件是deque[0] == nums[i-1], 将队首取出
            # 因为要保持deque和nums一致，当nums[i-1]是最大值被移除时，deque[0]也随之删除。
            if i > 0 and deque[0] == nums[i - 1]:
                deque.pop(0)  # 删除 deque 中对应的 nums[i-1]
            while deque and deque[-1] < nums[j]:
                deque.pop()  # 保持 deque 递减
            deque.append(nums[j])
            # print(deque)
            if i >= 0:
                res.append(deque[0])  # 记录窗口最大值
        return res


print(Solution1().maxSlidingWindow([1, 3, -1, -3, -2, 3, 6, 7], 3))
