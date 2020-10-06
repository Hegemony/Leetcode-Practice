"""
暴力解法
"""
def longestPalindrome(s):
    max_len = 0
    n = len(s)
    if n == 0:
        return ""
    if n == 1:  # 字符串长度为1
        return s
    def islongestpalindrmoestr(ss):
        if ss == ss[::-1]:  # 正序和倒序比较
            return True
        else:
            return False
    for i in range(n):
        for j in range(i+1, n+1):
            current = s[i:j]
            print(current)
            if islongestpalindrmoestr(current):
                cur_len = j-i
                if cur_len > max_len:
                    max_len = cur_len
                    result = current

    print(result)
    return result

longestPalindrome("babadaaabaa")

"""
动态规划解法
"""
n = 5
dp = [[False] * n for _ in range(n)]
print(dp)
