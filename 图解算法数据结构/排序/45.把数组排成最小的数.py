"""
枚举所有排列组合：超时
"""
class Solution:
    def minNumber(self, nums) -> str:
        result = []
        for i in nums:
            result.append(str(i))

        res = []
        result.sort()
        print(result)

        def helper(nums, temp):
            # 全排列
            if not nums:
                res.append(temp)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                helper(nums[:i] + nums[i + 1:], temp + [nums[i]])

        helper(result, [])
        res.sort()
        maxx = ''.join(res[0])
        for i in res:
            s = ''.join(i)
            maxx = min(maxx, s)
        return str(maxx)


"""
若拼接字符串 x + y > y + x ，则 m > n ；
反之，若 x + y < y + x ，则 n < m ；

利用冒泡排序就可以完成
"""


class Solution1:
    def minNumber(self, nums) -> str:
        n = len(nums)
        if n == 0:
            return ""
        for i in range(n):
            nums[i] = str(nums[i])
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return ''.join(nums)


a = [1, 3, 8, 5, 4, 2, 7]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            # print(a[i], a[j])
            a[j], a[i] = a[i], a[j]
            # print('-', a[i], a[j])
print(a)


class Solution2:
    def minNumber(self, nums) -> str:
        def fast_sort(l, r):
            if l >= r:
                return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j:
                    j -= 1
                    print('j:', j)
                    print(strs[j], strs[l])
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j:
                    i += 1
                    print('i:', i)
                    print(strs[i], strs[l])
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            fast_sort(l, i - 1)
            fast_sort(i + 1, r)

        strs = [str(num) for num in nums]
        fast_sort(0, len(strs) - 1)
        return ''.join(strs)


print(Solution2().minNumber([3, 30, 34, 5, 9]))
