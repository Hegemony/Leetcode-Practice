"""
暴力算法：超时
"""
def threeSum(nums):
    nums.sort()  # 排序关键
    # print(nums)
    result = []
    if len(nums) < 3:
        return []
    for i in range(len(nums)-2):

        for j in range(i+1, len(nums)-1):
            a = []
            a.append(nums[i])
            a.append(nums[j])
            sum2 = a[0] + a[1]

            for k in range(j+1, len(nums)):
                a.append(nums[k])
                print(a)
                if sum2 + a[2] == 0:
                    if a.copy() not in result:  # 去重复解
                        result.append(a.copy())
                    # print(result)
                    a.pop()
                else:
                    a.pop()
    print(result)
    return result

# nums = [-1, 0, 1, 2, -1, -4]
# threeSum(nums)

# for i in range(1, 2):
#     print(i)

def threeSum1(nums):
    nums.sort()  # 排序关键
    # print(nums)
    result = []
    n = len(nums)
    if n < 3:
        return []
    for i in range(n):
        if(nums[i] > 0):
            return result
        if (i > 0 and nums[i] == nums[i-1]):
            continue
        L = i + 1
        R = n-1
        while L < R:
            if(nums[i] + nums[L] + nums[R] == 0):
                result.append([nums[i], nums[L], nums[R]])
                while(L < R and nums[L] == nums[L+1]):
                    L = L + 1
                while(L < R and nums[R] == nums[R-1]):
                    R = R - 1
                L = L + 1
                R = R - 1
            elif(nums[i] + nums[L] + nums[R] > 0):
                R = R - 1
            else:
                L = L + 1
    # print(result)
    return result


def threeSum2(nums):
    nums.sort()
    result = []
    n = len(nums)
    if n < 3:
        return []
    for i in range(n - 2):
        if (nums[i] > 0):
            return result

        l = i + 1
        r = n - 1

        while l < r:
            if (nums[i] + nums[l] + nums[r] == 0):
                if [nums[i], nums[l], nums[r]] not in result:
                    result.append([nums[i], nums[l], nums[r]])
                    while (l < r and nums[l] == nums[l + 1]):
                        l = l + 1
                    while (l < r and nums[r] == nums[r - 1]):
                        r = r - 1
                l += 1
                r -= 1
            elif (nums[i] + nums[l] + nums[r] > 0):
                r -= 1
            else:
                l += 1

    return result

print(threeSum2([0, 0, 0, 0]))

