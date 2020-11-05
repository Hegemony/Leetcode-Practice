"""
我们考虑数组中的最后一个元素 x：在最小值右侧的元素，它们的值一定都小于等于 x；而在最小值左侧的元素，它们的值一定都大于等于 x。
因此，我们可以根据这一条性质，通过二分查找的方法找出最小值。
"""
class Solution:
    def minArray(self, numbers) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
                # return min(numbers[i:j])
        return numbers[i]
