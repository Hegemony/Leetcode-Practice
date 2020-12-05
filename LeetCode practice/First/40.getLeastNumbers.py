class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        import heapq
        heapq.heapify(arr)
        res = []
        for i in range(k):
            res.append(heapq.heappop())
        return res