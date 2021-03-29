class Solution:
    def singleNumbers(self, nums):
        ret = 0  # 所有数字异或的结果
        a = 0
        b = 0
        for n in nums:
            ret ^= n
        print(ret)
        # 找到第一位不是0的
        h = 1
        while (ret & h == 0):  # 找到第一位不是0的(从个位向十位，百位找)
            h <<= 1  # 依次向左移动，直到找到第一位1，以此为分类标准(因为该位不同，可以将两个结果分成两组)
        print('h:', h, bin(h))
        for n in nums:
            # 根据该位是否为0将其分为两组
            if (h & n == 0):
                a ^= n
                print('a:', a, bin(a))
            else:
                b ^= n
                print('b:', b, bin(b))
        return [a, b]


print(Solution().singleNumbers([4, 1, 4, 6]))
print(Solution().singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))
