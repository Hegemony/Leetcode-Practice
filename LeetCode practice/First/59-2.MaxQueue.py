class MaxQueue:

    def __init__(self):
        self.res = []
        self.flag = []

    def max_value(self) -> int:
        if self.flag:
            return self.flag[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.res.append(value)
        while self.flag and self.flag[-1] < value:
            self.flag.pop()
        self.flag.append(value)

    def pop_front(self) -> int:
        if len(self.res) != 0:
            result = self.res.pop(0)
            if result == self.flag[0]:
                self.flag.pop(0)
            return result
        else:
            return -1
# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
