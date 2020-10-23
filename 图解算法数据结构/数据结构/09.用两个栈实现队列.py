class CQueue:

    def __init__(self):
        self.res = []

    def appendTail(self, value: int) -> None:
        self.res.append(value)

    def deleteHead(self) -> int:
        if len(self.res) > 0:
            return self.res.pop(0)
        else:
            return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()