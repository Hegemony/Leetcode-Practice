class Solution:
    def exchange(self, nums):
        res1 = []
        res2 = []
        for i in nums:
            if i % 2 == 1:
                res1.append(i)
            if i % 2 == 0:
                res2.append(i)
        return res1 + res2


# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)
