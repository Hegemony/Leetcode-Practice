class Solution:
    def largestRectangleArea(self, heights) -> int:
        """
        暴力超时
        :param heights:
        :return:
        """
        # n = len(heights)
        # maxx = 0
        # for i in range(n):
        #     for w in range(1, n - i):
        #         minh = min(heights[i:w + i + 1])
        #         maxx = max(maxx, minh * w)
        # return maxx
        """
        找两边的比当前值小的左右边界,超时
        """
        # n = len(heights)
        # if not heights:
        #     return 0
        # left_i = [0 for _ in range(n)]  # 存i左边第一个小于heights[i]的下标
        # right_i = [0 for _ in range(n)]  # 存i右边第一个小于heights[i]的下标
        # left_i[0] = -1
        # right_i[-1] = n
        # for i in range(1, n):
        #     j = i - 1
        #     while j >= 0:
        #         if heights[j] < heights[i]:
        #             break
        #         else:
        #             j -= 1
        #     left_i[i] = j
        # for i in range(n - 2, -1, -1):
        #     j = i + 1
        #     while j < n:
        #         if heights[j] < heights[i]:
        #             break
        #         else:
        #             j += 1
        #     right_i[i] = j
        # print(left_i)
        # print(right_i)
        # res = 0
        # for i in range(n):
        #     res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
        # return res
        """
        单调栈
        """
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
