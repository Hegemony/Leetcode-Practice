"""
解题思路：
本问题是典型的矩阵搜索问题，可使用 深度优先搜索（DFS）+ 剪枝 解决。
深度优先搜索： 可以理解为暴力法遍历矩阵中所有字符串可能性。DFS 通过递归，先朝一个方向搜到底，再回溯至上个节点，沿另一个方向搜索，以此类推。
剪枝： 在搜索中，遇到 这条路不可能和目标字符串匹配成功 的情况（例如：此矩阵元素和目标字符不同、此元素已被访问），则应立即返回，称之为 可行性剪枝 。

DFS 解析：
递归参数： 当前元素在矩阵 board 中的行列索引 i 和 j ，当前目标字符在 word 中的索引 k 。

终止条件：
返回 false： (1) 行或列索引越界 或 (2) 当前矩阵元素与目标字符不同 或 (3) 当前矩阵元素已访问过 （ (3) 可合并至 (2) ） 。
返回 true： k = len(word) - 1 ，即字符串 word 已全部匹配。
递推工作：
标记当前矩阵元素： 将 board[i][j] 修改为 空字符 '' ，代表此元素已访问过，防止之后搜索时重复访问。
搜索下一单元格： 朝当前元素的 上、下、左、右 四个方向开启下层递归，使用 或 连接 （代表只需找到一条可行路径就直接返回，不再做后续 DFS ），
并记录结果至 res 。
还原当前矩阵元素： 将 board[i][j] 元素还原至初始值，即 word[k] 。
返回值： 返回布尔量 res ，代表是否搜索到目标字符串。

"""
class Solution:
    def exist(self, board, word: str) -> bool:
        def dfs(i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                # 如果路径出界或者矩阵中的值不是word中对应的字母，返回False
                return False
            if k == len(word) - 1:  # 如果单词已经检查完毕
                return True
            board[i][j] = ''   # 在一轮dfs中，搜索过的元素标记为''
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = word[k]   # 搜索过后还原为初始值，以便后续搜索。
            return res
        for i in range(len(board)):    # 矩阵每个结点做一遍dfs
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False