class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        res = []
        for i in range(len(nums)):
            heapq.heappush(res, -nums[i])
        print(res, nums)
        i = 0
        while i < k - 1:
            heapq.heappop(res)
            i += 1
        return -heapq.heappop(res)

import heapq

a = [3, 2, 5, 4, 6, 7]
heapq.heapify(a)
print(a)
heapq.heappush(a, 6)
print(a)
res = heapq.heappop(a)
print(res, a)
result1 = heapq.nsmallest(2, a)
result2 = heapq.nlargest(3, a)
print(result1, result2)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


arr = [12, 10, 11, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("排序后")
print(arr)
for i in range(n):
    print("%d" % arr[i])
