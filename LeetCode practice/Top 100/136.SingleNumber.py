"""
执行用时：1464 ms , 在所有 Python3 提交中击败了11.20%的用户
内存消耗：15 MB , 在所有 Python3 提交中击败了 33.83%的用户
"""
def singleNumber(nums):
    res = []
    for i in nums:
        if i not in res:
            res.append(i)
        else:
            res.remove(i)
    return res[0]

print(singleNumber([2, 2, 1]))
