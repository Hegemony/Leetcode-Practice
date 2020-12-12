class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_value = 0
        while i < j:
            cur_value = min(height[i], height[j]) * (j - i)
            if cur_value > max_value:
                max_value = cur_value

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_value