#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 将给定数组排序
# @param arr int整型一维数组 待排序的数组
# @return int整型一维数组
#
class Solution:
    def MySort(self, arr):
        # write code here
        """
        快速排序
        """
        # left, right = 0, len(arr) - 1
        # def qucik_sort(tmp, left, right):
        #     if left >= right:
        #         return
        #     low, high = left, right
        #     key = tmp[arr]
        #     while left < right:
        #         while left < right and tmp[right] > key:
        #             right -= 1
        #         tmp[left] = tmp[right]
        #         while left < right and tmp[left] <= key:
        #             left += 1
        #         tmp[right] = tmp[left]
        #     tmp[right] = key
        #     qucik_sort(tmp, low, right - 1)
        #     qucik_sort(tmp, left + 1, high)
        # qucik_sort(arr, left, right)
        """
        归并排序
        """

        def merge(left, right):
            res = []
            len1 = len(left)
            len2 = len(right)
            i, j = 0, 0
            while i < len1 and j < len2:
                if left[i] > right[j]:
                    res.append(right[j])
                    j += 1
                else:
                    res.append(left[i])
                    i += 1
            res += left[i:] if left[i:] else right[j:]
            return res

        def merge_sort(tmp):
            l = len(tmp)
            if l <= 1:
                return tmp
            mid = l // 2
            left = merge_sort(tmp[:mid])
            right = merge_sort(tmp[mid:])
            return merge(left, right)

        return merge_sort(arr)


print(Solution().MySort([5, 2, 3, 1, 4]))
