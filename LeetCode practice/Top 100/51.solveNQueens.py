class Solution:
    def solveNQueens(self, n):
        ans = []
        res = [['.' for i in range(n)] for i in range(n)]  # 保存最终的结果
        col = [False] * 2 * n  # 指示某一列是否可以放元素
        dg = [False] * 2 * n  # 指示对角线是否合法
        udg = [False] * 2 * n  # 指示反对角线是否合法

        def dfs(u):
            list_1 = []
            if u == n:
                for i in range(n):
                    list_1.append(''.join(res[i]))
                ans.append(list_1)
                return
            # 判断应该在哪一列放皇后
            for i in range(n):
                if not col[i] and not dg[u + i] and not udg[n - u + i]:
                    res[u][i] = 'Q'
                    col[i] = dg[u + i] = udg[n - u + i] = True
                    dfs(u + 1)
                    # 恢复现场
                    res[u][i] = '.'
                    col[i] = dg[u + i] = udg[n - u + i] = False

        # 从第0行开始搜
        dfs(0)
        return ans


"""
解法一：
用三个for
按行摆放：
"""


class Solution1:
    def solveNQueens(self, n):
        # 生成N*N的棋盘，填充棋盘，每个格子默认是“.”，表示没有放置皇后
        arr = [['.' for i in range(n)] for i in range(n)]
        res = []

        # 检查当前的行和列是否可以放置皇后
        def check(x, y):
            # 检查竖着的一列（从0 到 x 行）是否有皇后
            for i in range(x):
                if arr[i][y] == 'Q':
                    return False
            # 检查右下到左上的斜边是否有皇后
            i, j = x - 1, y - 1
            while i >= 0 and j >= 0:
                if arr[i][j] == 'Q':
                    return False
                i, j = i - 1, j - 1
            # 检查左下到右上的斜边是否有皇后
            i, j = x - 1, y + 1
            while i >= 0 and j < n:
                if arr[i][j] == 'Q':
                    return False
                i, j = i - 1, j + 1
            return True  # 如果三个方向都没有Q，则该位置可以放Q

        def dfs(x):
            # x是从0开始计算的
            # 当x == n时所有行的皇后放置完毕，记录结果
            if x == n:
                res.append([''.join(arr[i]) for i in range(n)])
                return
            # 遍历每一列
            for y in range(n):
                # 检查[x, y]这一坐标可以放置皇后
                # 如果满足条件，就放置皇后，并继续检查下一行
                if check(x, y):
                    arr[x][y] = 'Q'  # 设置为Q
                    dfs(x + 1)
                    arr[x][y] = '.'  # 进行回溯

        dfs(0)
        return res


print(Solution1().solveNQueens(4))

"""
解法二：
用三个集合
按行摆放：
"""


class Solution2:
    def solveNQueens(self, n):
        # 创建一个N行的数组，下标i对应N*N棋盘格子第i行的皇后位置
        arr = [-1 for i in range(n)]
        # 三个集合，分别判断某一列左斜线(左上到右下的斜线)，右斜线(左下到右上的斜线）
        columns = set()
        hypotenuse1 = set()
        hypotenuse2 = set()
        res = []

        def dfs(x):
            if x == n:
                # 如果x == n说明所有的皇后都摆放完了
                # 将arr数组中保存的结果拼接起来
                tmp = []
                row = ['.' for i in range(n)]
                for k in range(n):
                    row[arr[k]] = 'Q'
                    tmp.append(''.join(row))
                    row[arr[k]] = '.'
                res.append(tmp)
                return
            # 遍历一行中的每一列，并检查竖线、左斜线、右斜线是否有皇后
            for y in range(n):
                if y in columns:
                    continue
                if x - y in hypotenuse1:
                    continue
                if x + y in hypotenuse2:
                    continue
                # 如果检查通过，设置这一行的皇后位置，并将竖线、左斜线、右斜线的值放入集合中，并继续下一行递归
                # 当下一层的所有递归遍历完后，回到本轮需要将之前集合、arr数组中保存的结果都清空
                arr[x] = y
                columns.add(y)
                hypotenuse1.add(x - y)
                hypotenuse2.add(x + y)
                dfs(x + 1)
                arr[x] = -1
                columns.remove(y)
                hypotenuse1.remove(x - y)
                hypotenuse2.remove(x + y)

        dfs(0)
        return res
