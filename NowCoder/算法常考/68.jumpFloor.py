# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        dp = [1 for i in range(number + 1)]
        for i in range(2, number + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number]