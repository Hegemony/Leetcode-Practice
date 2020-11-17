class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 0:
            return False
        l = len(nums)
        cur_l = nums[0]
        for i in range(1, l):                    # i表示可以走到的位置
            if i <= cur_l:
                cur_l = max(cur_l, nums[i] + i)  # 判断当前位置可以走的最远的距离
            elif i > cur_l:                      # 如果超过这个距离，就停止，不能继续往下走
                return False
        return True


print(Solution().canJump([3, 2, 1, 0, 4]))
