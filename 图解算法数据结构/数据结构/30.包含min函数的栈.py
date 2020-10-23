class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.res = []

    def push(self, x: int) -> None:
        self.res.append(x)

    def pop(self) -> None:
        self.res.pop()

    def top(self) -> int:
        return self.res[-1]

    def min(self) -> int:
        return min(self.res)

"""
push(x) 函数： 重点为保持栈 B 的元素是 非严格降序 的；

执行「元素 x 压入栈 A」 ；
若「栈 B 为空」或「x \leq≤ 栈 B 的栈顶元素」，则执行「元素 x 压入栈 B」 ；
pop() 函数： 重点为保持栈 A , B 的 元素一致性 ；

执行「栈 A 元素出栈」，将出栈元素记为 y ；
若 「y 等于栈 B 的栈顶元素」，则执行「栈 B 元素出栈」；
top() 函数： 直接返回栈 A 的栈顶元素，即返回 A.peek() ；

min() 函数： 直接返回栈 B 的栈顶元素，即返回 B.peek() ；
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or x <= self.B[-1]:
            self.B.append(x)

    def pop(self) -> None:
        res = self.A.pop()
        if res == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]