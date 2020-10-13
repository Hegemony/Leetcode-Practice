"""
利用字典的方法，速度较慢
"""
class Solution:
    def search(self, nums, target) -> int:
        dic = {}
        n = len(nums)
        for i in range(n):
            dic[nums[i]] = dic.get(nums[i], 0) + 1

        if target in dic.keys():
            return dic[target]
        else:
            return 0


"""
题解做法：
解题思路：
排序数组中的搜索问题，首先想到 二分法 解决。

初始化： 左边界 i = 0，右边界 j = len(nums) - 1。
循环二分： 当闭区间 [i, j] 无元素时跳出；
计算中点 m = (i + j) / 2 （向下取整）；
若 nums[m] < target ，则 targettarget 在闭区间 [m + 1, j]中，因此执行 i = m + 1；
若 nums[m] > target ，则 targettarget 在闭区间 [i, m - 1] 中，因此执行 j = m - 1；
若 nums[m] = target ，则右边界 rightright 在闭区间 [m+1, j] 中；左边界 left 在闭区间 [i, m-1] 中。因此分为以下两种情况：
若查找 右边界 right ，则执行 i = m + 1 ；（跳出时 i 指向右边界）
若查找 左边界 left ，则执行 j = m - 1 ；（跳出时 j 指向左边界）
返回值： 应用两次二分，分别查找 rightright 和 left ，最终返回 right - left - 1 即可。

"""
class Solution1:
    def search(self, nums, target) -> int:
        # 搜索右边界
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            elif nums[m] == target:  # 等于的情况，因为要找右边界，所以要右移
                i = m + 1
            else:
                j = m - 1
        right = i

        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target:
            return 0

        # 如果这里能够运行, 肯定是找到了target的
        i = 0
        # 搜索左边界
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            elif nums[m] == target:  # 等于的情况，因为要找左边界，所以要左移
                j = m - 1
            else:
                j = m - 1
        left = j
        return right - left - 1

"""
二分查找模板：二分查找得到下界
"""
def lower_bound(nums: list, target: int) -> int:
    '''
    return the target lower bound index in nums
    '''
    first, last = 0, len(nums)
    while first < last:
        mid = first + (last - first) // 2  # 防溢出
        # 注意此处是小于号
        if nums[mid] < target:
            first = mid + 1
        else:
            last = mid
    return first
# 返回的first 如果等于数组长度或者对应位置索引不等于目标值,那么说明没有找到


"""
二分查找模板：二分查找得到上界
"""
def upper_bound(nums: list, target: int) -> int:
    '''
    return the first idx in nums when nums[idx] > target
    '''
    first, last = 0, len(nums)
    while first < last:
        mid = first + (last - first) // 2
        # 注意直接把 < 改成 <=
        if nums[mid] <= target:
            first = mid + 1
        else:
            last = mid
    return first
# 该函数返回的是第一个大于目标值的索引, 如果返回0或者该索引前一个位置的值不是目标值,
