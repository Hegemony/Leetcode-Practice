"""
哈希 + sort
"""


class Solution:
    def topKFrequent(self, nums, k):
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        res = []
        for i in dic.values():
            res.append(i)
        res.sort()
        res.reverse()
        print(res)
        result = []
        for i in range(k):
            for j in dic:
                if dic[j] == res[i]:
                    result.append(j)
                    dic[j] = float('inf')
        return result


"""
哈希 + 堆
"""

import heapq


class Solution1:
    def topKFrequent(self, nums, k):
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        res = []
        for i in dic:
            heapq.heappush(res, (-dic[i], i))  # heapq.heappush可以传入一个元组，默认使用元组第一个元素进行排序
        result = []
        for i in range(k):
            result.append(heapq.heappop(res)[1])
        return result


print(Solution1().topKFrequent([1, 2], 2))
