"""
暴力超时：
"""


class Solution:
    def subarraySum(self, nums, k):
        l = len(nums)
        count = 0
        for i in range(l + 1):
            summ = 0
            for j in range(i, l):
                summ += nums[j]
                print(',', summ)
                if summ == k:
                    count += 1
        return count


# print(Solution().subarraySum([1, 2, 3], 3))

"""
前缀和:超时
"""


class Solution1:
    def subarraySum(self, nums, k):
        count = 0
        l = len(nums)
        pre = [0 for i in range(l + 1)]
        for i in range(1, l + 1):
            pre[i] = pre[i - 1] + nums[i - 1]  # pre列表中第一个数为0，从索引1开始每个数是该列表当前索引之前的前缀和
        for i in range(1, l + 1):
            for j in range(i, l + 1):
                if (pre[j] - pre[i - 1] == k):
                    count += 1
        print(pre)
        return count


print(Solution1().subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))

"""
前缀和 + 哈希表:
hashmap 的 key 为前缀数，value 为前缀数出现的次数
i 在 j 前面，k已知，pre[i] = pre[j] - k

以及先遍历i，那么i在j前面，k已知，那么就可以有点类似于2sum的题，当我拿到pre[j]的值的时候，
我去检查曾经是否有pre[j]-k也就是pre[i]出现过，如果出现过，就说明存在从prefixSum[i]到prefixSum[j]的距离为k的情况
"""


class Solution2:
    def subarraySum(self, nums, k):
        count = 0
        dic = {0: 1}
        pre = 0
        for num in nums:
            pre += num
            tmp = pre - k
            if tmp in dic:  # 如果 pre[j] - k 在字典中，说明出现过前缀和为k的一段序列，出现过的次数为字典中的value
                count += dic[tmp]

            dic[pre] = dic.get(pre, 0) + 1  # 每个pre，也就是前缀和需要放入到字典中
        return count
