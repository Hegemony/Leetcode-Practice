class Solution:
    def getLeastNumbers(self, arr, k: int):
        arr.sort()
        return arr[:k]