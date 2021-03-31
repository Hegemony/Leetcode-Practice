class MaxQueue:

    def __init__(self):
        self.q = []
        self.res = []

    def max_value(self) -> int:
        if self.res:
            return self.res[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.res and self.res[-1] < value:
            self.res.pop()
        self.res.append(value)

    def pop_front(self) -> int:
        if self.q:
            result = self.q.pop(0)
            if result == self.res[0]:
                self.res.pop(0)
            return result
        else:
            return -1

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
