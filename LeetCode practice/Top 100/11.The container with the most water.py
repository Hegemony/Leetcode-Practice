"""
暴力解法：超出时间限制
"""
def maxArea(height):
    max_area = 0
    for i in range(len(height) - 1):
        for j in range(i+1, len(height)):
            a = height[i:j+1]
            print(a)
            s = min(a[0], a[len(a)-1])
            cur_area = s * (j-i)

            if cur_area > max_area:
                max_area = cur_area
    # print(max_area)
    return max_area

maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])

# a = [1, 2, 3]
# print(len(a))
# for i in range(len(a)):   # 正序
#     print(i)
#
# for i in range(len(a)-1, -1, -1):  # 倒序
#     print(i)
#
# print(a[1:2])

"""
双指针法：O(N)
"""
def maxArea1(height):
    max_area = 0
    i, j = 0, len(height)-1
    while i < j:
        cur_area = min(height[i], height[j]) * (j - i)
        if cur_area > max_area:
            max_area = cur_area

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    print(max_area)
    return max_area

maxArea1([1, 8, 6, 2, 5, 4, 8, 3, 7])