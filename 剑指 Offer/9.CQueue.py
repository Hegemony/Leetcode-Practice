class CQueue:

    def __init__(self):
        self.res = []

    def appendTail(self, value: int) -> None:
        self.res.append(value)
        return None

    def deleteHead(self) -> int:
        if self.res:
            result = self.res[0]
            self.res.pop(0)
            return result
        else:
            return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()