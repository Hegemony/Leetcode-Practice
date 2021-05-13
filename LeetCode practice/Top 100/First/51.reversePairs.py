class Solution:
    def merge(self, left, right):
        tmp = []
        len1 = len(left)
        len2 = len(right)
        i, j = 0, 0
        while i < len1 and j < len2:
            if left[i] > right[j]:
                self.res += (len1 - i)
                tmp.append(right[j])
                j += 1
            else:
                tmp.append(left[i])
                i += 1
        tmp += left[i:] if left[i:] else right[j:]
        return tmp

    def mergeSort(self, nums):
        l = len(nums)
        if l <= 1:
            return nums
        mid = l // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)

    def reversePairs(self, nums) -> int:
        self.res = 0
        self.mergeSort(nums)
        return self.res
