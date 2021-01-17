class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2 ** 31, 2 ** 31 - 1
        flag = 1
        if dividend < 0:
            flag, dividend = -flag, -dividend
        if divisor < 0:
            flag, divisor = -flag, -divisor
        cnt = 0
        while dividend >= divisor:
            cur = divisor  # 第一次是cur = divisor
            mul = 1
            while cur + cur <= dividend:
                cur += cur  # 这里是将cur x 2，即直接比较divisor x 2的次方（加快比较速度）
                mul += mul  # 保留divisor的倍数
            dividend -= cur  # dividend 变为 dividend-cur 进行下一轮while
            cnt += mul

        cnt = cnt if flag > 0 else -cnt  # 还原商的正负

        if cnt < MIN_INT:
            return MIN_INT
        elif cnt > MAX_INT:
            return MAX_INT
        else:
            return cnt   