"""
二进制运算异或题解：
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/zhi-chu-xian-yi-ci-de-shu-xi-lie-wei-yun-suan-by-a/
"""


class Solution:
    def singleNumbers(self, nums):
        ret = 0  # 所有数字异或的结果
        a = 0
        b = 0
        for n in nums:
            ret ^= n
        # 找到第一位不是0的
        h = 1
        while (ret & h == 0):  # 找到第一位不是0的
            h <<= 1            # 依次向左移动，直到找到第一位1，以此为分类标准
            print('h:', bin(h))
        for n in nums:
            # 根据该位是否为0将其分为两组  ，
            """
            因为前面数组中的所有数都进行异或运算，导致结果出现1那位肯定有只出现一次的数在相对应的位置为1，另一个只出现
            一次的数在相对应的位置为0。
            """
            if (h & n == 0):
                a ^= n
                print('a:', bin(a))
            else:
                b ^= n
                print('b:', bin(b))
        return [a, b]


print(Solution().singleNumbers([4, 2, 4, 6]))
# print(Solution().singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))
