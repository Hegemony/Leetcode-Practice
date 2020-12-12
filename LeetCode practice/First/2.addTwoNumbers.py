# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        res1 = []
        while p:
            res1.append(p.val)
            p = p.next
        res1.reverse()
        q = l2
        res2 = []
        while q:
            res2.append(q.val)
            q = q.next
        res2.reverse()

        first = 0
        for i in range(len(res1)):
            first = first * 10 + res1[i]

        second = 0
        for i in range(len(res2)):
            second = second * 10 + res2[i]

        summ = first + second  # 807

        l3 = ListNode(0)
        m = l3
        while summ:   # 7 - 0 - 8
            cnt = summ % 10
            newnode = ListNode(cnt)
            m.next = newnode
            m = m.next
            summ //= 10
        return l3.next