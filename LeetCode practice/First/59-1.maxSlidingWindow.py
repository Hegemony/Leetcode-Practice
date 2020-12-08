class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        i, j = 0, k - 1
        res = []
        while j < n:
            tmp = max(nums[i:j + 1])
            res.append(tmp)
            j += 1
            i += 1
        return res