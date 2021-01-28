"""
多重背包模板：
多重背包本质和01背包一样，只不过每个物品增加了可选的数据，
可将所有物品都展开，都当做是不同的物品，再用01背包问题求解。
"""

# weightList：每种物品的体积
# valueList：每种物品的价值
# numList：每种物品的数量


def trans(weightList, valueList, numList):
    # 转换函数
    K = len(numList)
    newWeightList = []
    newValueList = []
    num = sum(numList)
    for i in range(K):
        for j in range(numList[i]):
            newWeightList.append(weightList[i])
            newValueList.append(valueList[i])
    return num, newValueList, newWeightList


def zeroOneBag(numList, capacity, weightList, valueList):
    # 先将多重背包问题转成0-1背包问题，利用0-1背包问题的代码。
    num, newValueList, newWeightList = trans(weightList, valueList, numList)
    valueExcel = [[0 for j in range(capacity + 1)] for i in range(num + 1)]
    for i in range(1, num + 1):
        for j in range(1, capacity + 1):
            valueExcel[i][j] = valueExcel[i - 1][j]
            if j >= newWeightList[i - 1]:
                valueExcel[i][j] = max(valueExcel[i - 1][j], valueExcel[i - 1][j - newWeightList[i - 1]] + newValueList[i - 1])
            else:
                valueExcel[i][j] = valueExcel[i - 1][j]
    return valueExcel


print(zeroOneBag([2, 5, 10], 8, [2, 2, 1], [20, 10, 6]))

# 输出结果：
# [[0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 20, 20, 20, 20, 20, 20, 20],
# [0, 0, 20, 20, 40, 40, 40, 40, 40],
# [0, 0, 20, 20, 40, 40, 50, 50, 50],
# [0, 0, 20, 20, 40, 40, 50, 50, 60],
# [0, 0, 20, 20, 40, 40, 50, 50, 60],
# [0, 0, 20, 20, 40, 40, 50, 50, 60],
# [0, 0, 20, 20, 40, 40, 50, 50, 60],
# [0, 6, 20, 26, 40, 46, 50, 56, 60],
# [0, 6, 20, 26, 40, 46, 52, 56, 62],
# [0, 6, 20, 26, 40, 46, 52, 58, 62],
# [0, 6, 20, 26, 40, 46, 52, 58, 64],
# [0, 6, 20, 26, 40, 46, 52, 58, 64],
# [0, 6, 20, 26, 40, 46, 52, 58, 64],
# [0, 6, 20, 26, 40, 46, 52, 58, 64],
# [0, 6, 20, 26, 40, 46, 52, 58, 64],
# [0, 6, 20, 26, 40, 46, 52, 58, 64],
# [0, 6, 20, 26, 40, 46, 52, 58, 64]]
