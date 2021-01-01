class Solution:
    def removeElement(self, nums, val):
        l = nums.count(val)
        for i in range(l):
            nums.remove(val)
        return nums


print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
