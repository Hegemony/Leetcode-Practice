class UnionFind:
    def __init__(self):
        self.father = {}
        # 统计数量
        self.nums = 0

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            # 集合的数量+1
            self.nums += 1

    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_x:
            self.father[root_x] = root_y
            # 集合的数量-1
            self.nums -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findCircleNum(self, isConnected) -> int:
        uf = UnionFind()
        for i in range(len(isConnected)):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    uf.merge(i, j)
        return uf.nums