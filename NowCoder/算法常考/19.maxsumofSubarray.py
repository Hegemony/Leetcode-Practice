#
# max sum of the subarray
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxsumofSubarray(self, arr):
        # write code here
        dp = [0 for i in range(len(arr))]
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            if dp[i - 1] + arr[i] > arr[i]:
                dp[i] = dp[i - 1] + arr[i]
            else:
                dp[i] = arr[i]
        return max(dp)