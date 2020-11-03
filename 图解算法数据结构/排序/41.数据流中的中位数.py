"""
暴力：超时
"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.res = []
        self.result = []
        self.l = 0
    def addNum(self, num: int) -> None:
        self.res.append(num)
        self.result = self.res.copy()
        self.l = len(self.result)
    def findMedian(self) -> float:
        self.result.sort()
        if self.l % 2 == 0:
            return (self.result[self.l // 2] + self.result[self.l // 2 - 1]) / 2.0
        if self.l % 2 == 1:
            return self.result[self.l // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
堆的操作：
import heapq

heapq.heappush(heap, x)      # 将x压入堆中
                                    
heapq.heappop(heap)          # 从堆中弹出最小的元素 
                                
heapq.heapify(heap)          # 让列表具备堆特征  
                                    
heapq.heapreplace(heap, x)   # 弹出最小的元素，并将x压入堆中  
                         
heapq.nlargest(n, iter)      # 返回iter中n个最大的元素 
                                      
heapq.nsmallest(n, iter)     # 返回iter中n个最小的元素                              

max_column_data = heapq.nlargest(1, temp_list, key=lambda item: len(item))   # 从一个list中获取最大的元素
"""
"""
Python 中 heapq 模块是小顶堆。
实现" 大顶堆 "方法： 小顶堆的插入和弹出操作均将元素" 取反 "即可。
"""
from heapq import *
class MedianFinder1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []    # 小顶堆，存较大的数
        self.B = []    # 大顶堆，存较小的数
    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))   # 把小顶堆A的小数放入到大顶堆B中
        else:
            heappush(self.B, -num)      # 取反是因为headpush默认是小顶堆，加个负号，大数变小数，变相实现了小顶堆
            heappush(self.A, -heappop(self.B))  # 大顶堆B的大数放入到小顶堆A中
    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
python_bisect模块的使用
这个模块只有几个函数，

一旦决定使用二分搜索时，立马要想到使用这个模块　

import bisect  

x_insert_point = bisect.bisect_left(L,x)　　 # 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置 
  
x_insert_point = bisect.bisect_right(L,x)   # 在L中查找x，x存在时返回x右侧的位置，x不存在返回应该插入的位置
 
x_insort_left = bisect.insort_left(L,x)     # 将x插入到列表L中，x存在时插入在左侧  

x_insort_rigth = bisect.insort_right(L,x)   # 将x插入到列表L中，x存在时插入在右侧　　　　  

"""
import bisect
class MedianFinder2:

    def __init__(self):
        self.d = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.d, num)

    def findMedian(self) -> float:
        return (self.d[len(self.d) // 2] + self.d[(len(self.d) - 1) // 2]) / 2
