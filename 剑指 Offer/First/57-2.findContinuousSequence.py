class Solution:
    def findContinuousSequence(self, target: int):
        i, j = 1, 1
        res = []
        while j < (target + 1) // 2 + 1:
            summ = sum(list(range(i, j + 1)))
            if summ < target:  # 若和小于目标，右指针向右移动，扩大窗口
                j += 1
            elif summ == target:  # 相等就把指针形成的窗口添加进输出列表中
                res.append(list(range(i, j + 1)))
                i += 1
                j += 1
            else:  # 若和大于目标，左指针向右移动，减小窗口
                i += 1
        return res