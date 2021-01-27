"""
01背包模板：
f[i][j] 表示只看前i个物品，总体积是j的情况下，总价值最大是多少。

result = max(f[n][0~V]) f[i][j]:
不选第i个物品：f[i][j] = f[i-1][j];
选第i个物品：f[i][j] = f[i-1][j-v[i]] + w[i]（v[i]是第i个物品的体积） 两者之间取最大。

初始化：f[0][0] = 0 （啥都不选的情况，不管容量是多少，都是0）
"""


def bag(n, z, w, v):
    """
    测试数据：
    n = 6  物品的数量，
    z = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(z + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, z + 1):
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换， i-1代表第i个物品
            if j >= w[i - 1]:  # 由上一行同一列变换过来，或者由上一行，前几列+当前价值变换过来
                value[i][j] = max(value[i - 1][j], value[i - 1][j - w[i - 1]] + v[i - 1])
                # j - w[i - 1] 表示要放当前的物品，找之前没有j-w[i]的空间时的最大价值
            else:
                value[i][j] = value[i - 1][j]
    for x in value:
        print(x)
    return value


"""
显示第几个物品被选中
"""


def show(n, z, w, value):
    print('最大价值为:', value[n][z])
    x = [False for i in range(n)]
    j = z
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i + 1, '个,', end='')
    print('\n')


"""
优化空间复杂度后：
"""


def bag1(n, z, w, v):
    values = [0 for i in range(z + 1)]
    for i in range(1, n + 1):
        for j in range(z, 0, -1):  # 逆序，从后往前更新, 因为在二维dp中当前行只与上一行有关系，所以从后向前遍历，利用上一行前面的值
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1]:
                values[j] = max(values[j - w[i - 1]] + v[i - 1], values[j])
        print(values)
    return values


if __name__ == '__main__':
    n = 6
    z = 10
    w = [2, 2, 3, 1, 5, 2]  # 重量
    v = [2, 3, 1, 5, 4, 3]  # 价值
    value = bag(n, z, w, v)
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # [0, 0, 3, 3, 5, 5, 5, 5, 5, 5, 5]
    # [0, 0, 3, 3, 5, 5, 5, 6, 6, 6, 6]
    # [0, 5, 5, 8, 8, 10, 10, 10, 11, 11, 11]
    # [0, 5, 5, 8, 8, 10, 10, 10, 12, 12, 14]
    # [0, 5, 5, 8, 8, 11, 11, 13, 13, 13, 15]
    show(n, z, w, value)
    # 最大价值为: 15
    # 背包中所装物品为:
    # 第 2 个,第 4 个,第 5 个,第 6 个,
    print('\n空间复杂度优化为N(c)结果:', bag1(n, z, w, v))
    # 空间复杂度优化为N(c)结果: [0, 5, 5, 8, 8, 11, 11, 13, 13, 13, 15]
