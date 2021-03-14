# -*- coding:utf-8 -*-
import heapq


class Finder:
    def findKth(self, a, n, K):
        res = []
        for i in range(n):
            heapq.heappush(res, -a[i])
        i = 0
        while i < K:
            if i == K - 1:
                return -heapq.heapify(res)
            heapq.heappop(res)
            i += 1
