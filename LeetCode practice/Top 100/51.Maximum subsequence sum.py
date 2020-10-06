"""
暴力解1：枚举所有可能->超时
"""


def maxSubArray(nums):
    n = len(nums)
    # max_result = float('inf')  # 正无穷
    max_result = float('-inf')  # 负无穷

    for i in range(n):
        for j in range(i + 1, n + 1):
            res = nums[i:j]
            cur_result = sum(res)

            if cur_result > max_result:
                max_result = cur_result

    return max_result


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

"""
暴力解法2：超时
"""
def maxSubArray1(nums):
    n = len(nums)
    # max_result = float('inf')  # 正无穷
    max_result = float('-inf')  # 负无穷


    for i in range(n):
        cur_result = 0
        for j in range(i, n):
            cur_result += nums[j]

            if cur_result > max_result:
                max_result = cur_result
    return max_result


print(maxSubArray1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

"""
动态规划方法：
dp[i]：表示以 nums[i] 结尾的连续子数组的最大和。
状态转移方程:
dp[i]=max{nums[i],dp[i−1]+nums[i]}
"""
def maxSubArray2(nums):
    n = len(nums)
    dp = [0 for i in range(n)]

    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
    return max(dp)

