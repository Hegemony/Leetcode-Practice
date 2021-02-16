class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        """
        利用sort, O(nlogn)
        :param nums1:
        :param nums2:
        :return:
        """
        # res = nums1 + nums2
        # res.sort()
        # l = len(res)
        # return res[l // 2] if l % 2 == 1 else (res[l // 2] + res[l // 2 - 1]) / 2
        """
        利用归并排序, O(N)
        """
        res = []
        l1, l2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < l1 and j < l2:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        res += nums1[i:] if nums1[i:] else nums2[j:]
        l = len(res)
        return res[l // 2] if l % 2 == 1 else (res[l // 2] + res[l // 2 - 1]) / 2
