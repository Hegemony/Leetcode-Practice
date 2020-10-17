class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()  # 先进行排序
        n = len(nums)
        s = nums.count(0)  # 统计0的个数
        l = s
        r = n - 1
        i, j = s, s + 1
        while i < j and i < n - 1:  # 判断去零后的列表是否有重复数字
            if nums[i] == nums[j]:
                return False
            else:
                i += 1
                j += 1

        if nums[r] - nums[l] <= 4:  # 去零后的列表最大和最小数之间的差距不超过4
            return True
        else:
            return False


# a = [1, 2, 3]
# print(a.count(0))

print(Solution().isStraight([11, 0, 9, 0, 0]))

"""
题解：利用set()
"""
class Solution:
    def isStraight(self, nums) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0:
                continue  # 跳过大小王
            ma = max(ma, num)  # 最大牌
            mi = min(mi, num)  # 最小牌
            if num in repeat:
                return False  # 若有重复，提前返回 false
            repeat.add(num)  # 添加牌至 Set
        return ma - mi < 5  # 最大牌 - 最小牌 < 5 则可构成顺子
