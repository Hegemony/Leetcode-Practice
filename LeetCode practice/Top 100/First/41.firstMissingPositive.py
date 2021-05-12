class Solution:
    def firstMissingPositive(self, nums) -> int:
        """
        O(nlogn) + O(1)的解法
        :param nums:
        :return:
        """
        # nums.sort()
        # target = 1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         target += 1
        # return target
        """
        O(n) + O(n)的解法
        """
        # dic = {}
        # for i in range(len(nums)):
        #     dic[nums[i]] = 1
        # for i in range(1, len(nums) + 2):
        #     if i not in dic:
        #         return i
        """
        O(n) + O(1)的解法
        """
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1  # 这里只要大于等于n + 1就行，保证缺失的数在[1, N + 1]内
        # print(nums)
        # 出现的元素对应的索引的数字都是负数
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # 找到负数的话，答案是该位置的索引 + 1
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        # 没有负数的话，答案是N + 1
        return n + 1


print(Solution().firstMissingPositive([3, 4, -1, -2, 1, 5, 16, 0, 2, 0]))
