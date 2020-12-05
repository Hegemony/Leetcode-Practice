import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []  # 小顶堆存储较大的一部分数
        self.b = []  # 大顶堆存储较小的一部分数

    def addNum(self, num: int) -> None:
        if len(self.a) != len(self.b):
            heapq.heappush(self.a, num)
            heapq.heappush(self.b, -heapq.heappop(self.a))
        else:
            heapq.heappush(self.b, -num)
            heapq.heappush(self.a, -heapq.heappop(self.b))

    def findMedian(self) -> float:
        return self.a[0] if len(self.a) != len(self.b) else (self.a[0] - self.b[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
