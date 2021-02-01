"""
https://leetcode-cn.com/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/
并查集是一种数据结构:
并查集这三个字，一个字代表一个意思。
1.并（Union），代表合并
2.查（Find），代表查找
3.集（Set），代表这是一个以字典为基础的数据结构，它的基本功能是合并集合中的元素，查找集合中的元素
并查集的典型应用是有关连通分量的问题
并查集解决单个问题（添加，合并，查找）的时间复杂度都是O(1)O(1)
因此，并查集可以应用到在线算法中

并查集的实现:
并查集跟树有些类似，只不过她跟树是相反的。在树这个数据结构里面，每个节点会记录它的子节点。在并查集里，每个节点会记录它的父节点。
"""


class UnionFind:

    def __init__(self):
        """
        记录每个节点的父节点
        """
        self.father = {}

    def add(self, x):
        """
        初始化:
        当把一个新节点添加到并查集中，它的父节点应该为空
        添加新节点
        """
        if x not in self.father:
            self.father[x] = None

    def merge(self, x, y):
        """
        合并两个节点:
        如果发现两个节点是连通的，那么就要把他们合并，也就是他们的祖先是相同的。这里究竟把谁当做父节点一般是没有区别的。
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y

    def is_connected(self, x, y):
        """
        判断两节点是否相连:
        判断两个节点是否处于同一个连通分量的时候，就需要判断它们的祖先是否相同
        """
        return self.find(x) == self.find(y)

    def find(self, x):
        """
        查找祖先:
        查找祖先的方法是：如果节点的父节点不为空，那就不断迭代。
         + 路径压缩
        """
        root = x
        while self.father[root] != None:
            root = self.father[root]

        # 路径压缩：使得路径深度恒定为2
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root
