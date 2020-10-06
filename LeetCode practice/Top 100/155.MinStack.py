class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.res = []
        self.a = 0
        self.c = []

    def push(self, x: int) -> None:
        self.res.append(x)

    def pop(self) -> None:
        a = self.res[-1]
        self.res.pop(-1)
        return a

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        c = self.res.copy()
        c.sort()
        return c[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()