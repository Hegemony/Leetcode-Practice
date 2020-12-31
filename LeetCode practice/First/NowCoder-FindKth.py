import heapq


class Finder:
    def findKth(self, a, n, K):
        res = []
        for i in range(n):
            heapq.heappush(res, -a[i])

        i = 0
        while i < K:
            if i == K - 1:
                return -heapq.heappop(res)
            heapq.heappop(res)
            i += 1


class Finder1:
    def findKth(self, a, n, K):
        k = n - K
        low = 0
        high = n - 1
        while low <= high:
            p = self.patition(a, low, high)
            if k < p:
                high = p - 1
            elif k > p:
                low = p + 1
            else:
                return a[p]
        return -1

    def patition(self, alist, low, high):
        mid_value = alist[low]
        while low < high:
            while low < high and alist[high] > mid_value:
                high -= 1
            alist[low] = alist[high]

            while low < high and alist[low] <= mid_value:
                low += 1
            alist[high] = alist[low]
        alist[low] = mid_value
        return low
