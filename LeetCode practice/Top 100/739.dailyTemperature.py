"""
暴力超时
"""


class Solution:
    def dailyTemperature(self, T):
        res = []
        for i in range(len(T)):
            flag = 0
            for j in range(i + 1, len(T)):
                if T[j] > T[i]:
                    flag += 1
                    res.append(j - i)
                    break
            if flag == 0:
                res.append(0)
        return res


# print(Solution().dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73, 80]))

"""
单调栈做法:
栈是单调递减的
"""


class Solution1:
    def dailyTemperature(self, T):
        l = len(T)
        res =[0 for i in range(l)]
        stack = []   # 栈存储的是温度的索引
        for i in range(l):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()  # 遇到比栈顶温度高的数，就弹出栈顶，直至栈内元素大于该元素，或者栈为空
                res[prev_index] = i - prev_index  # 弹出的索引对应该温度需要等待的天数
            stack.append(i)
        return res