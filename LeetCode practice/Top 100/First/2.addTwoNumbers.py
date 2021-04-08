# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        res1, res2 = [], []
        while p:
            res1.append(p.val)
            p = p.next
        res1.reverse()
        while q:
            res2.append(q.val)
            q = q.next
        res2.reverse()

        first, second = 0, 0
        for i in range(len(res1)):
            first = 10 * first + res1[i]
        for i in range(len(res2)):
            second = 10 * second + res2[i]
        summ = first + second

        if summ == 0:
            return ListNode(0)
        l = ListNode(0)
        m = l
        while summ:
            cnt = summ % 10
            newnode = ListNode(cnt)
            m.next = newnode
            m = m.next
            summ //= 10
        return l.next