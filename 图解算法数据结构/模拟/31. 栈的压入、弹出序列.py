"""
初始化： 辅助栈 stack ，弹出序列的索引 ii ；
遍历压栈序列： 各元素记为 num ；
元素 num 入栈；
循环出栈：若 stack 的栈顶元素 == 弹出序列元素 popped[i] ，则执行出栈与 i++i++ ；
返回值： 若 stack 为空，则此弹出序列合法。

"""
class Solution:
    def validateStackSequences(self, pushed, popped):
        res = []
        m = 0
        for i in range(len(pushed)):
            res.append(pushed[i])
            while res and res[-1] == popped[m]:
                res.pop()
                m += 1
        if res:
            return False
        else:
            return True