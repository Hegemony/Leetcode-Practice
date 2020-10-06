class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = 0
        for i in nums:
            if i == 0:
                n += 1
        for j in range(n):
            nums.remove(0)
        for j in range(n):
            nums.append(0)
        return nums

# print(Solution().moveZeroes([0, 0, 1]))

print(Solution().moveZeroes([0, 1, 0, 3, 12]))

# a = [10, 20, 30]
# b = a.pop(1)
# a.remove(30)
# print(b)
# print(a)
