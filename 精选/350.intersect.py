class Solution:
    def intersect(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        dic = {}
        res = []
        l = min(len1, len2)
        if l == len1:
            for i in range(len(nums1)):
                dic[nums1[i]] = dic.get(nums1[i], 0) + 1
            for i in range(len(nums2)):
                if nums2[i] in dic and dic[nums2[i]] > 0:
                    res.append(nums2[i])
                    dic[nums2[i]] -= 1
        else:
            for i in range(len(nums2)):
                dic[nums2[i]] = dic.get(nums2[i], 0) + 1
            for i in range(len(nums1)):
                if nums1[i] in dic and dic[nums1[i]] > 0:
                    res.append(nums1[i])
                    dic[nums1[i]] -= 1
        return res
