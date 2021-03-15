#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self, arr):
        # if len(arr) < 2:
        #     return len(arr)
        # l, r = 0, 0
        # res = 1
        # while r < len(arr) - 1:
        #     r += 1
        #     if arr[r] not in arr[l:r]:
        #         res = max(r - l + 1, res)
        #     else:
        #         while arr[r] in arr[l:r]:
        #             l += 1
        # return res
        if len(arr) < 2:
            return len(arr)
        dic = {}
        l = -1
        res = 0
        for i in range(len(arr)):
            if arr[i] in dic:
                l = max(dic[arr[i]], l)
            dic[arr[i]] = i
            res = max(res, i - l)
        return res