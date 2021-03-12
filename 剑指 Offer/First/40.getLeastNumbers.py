class Solution:
    def getLeastNumbers(self, arr, k: int):
        import heapq
        heapq.heapify(arr)
        res = []
        for i in range(k):
            res.append(heapq.heappop(arr))
        return res