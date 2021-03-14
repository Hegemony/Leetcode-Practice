# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        l = len(tinput)
        if l < k:
            return []
        import heapq
        res = []
        heapq.heapify(tinput)
        for i in range(k):
            res.append(heapq.heappop(tinput))
        return res


print(Solution().GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 5))
