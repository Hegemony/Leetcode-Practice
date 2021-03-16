class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head ListNode类
# @param n int整型
# @return ListNode类
#
class Solution:
    def removeNthFromEnd(self, head, n):
        # write code here
        p = head
        cnt = 0
        while p:
            p = p.next
            cnt += 1
        dummpy = ListNode(0)
        dummpy.next = head
        p = dummpy
        res = 0
        while p:
            if res == cnt - n + 1:
                p.next = p.next.next
                break
            res += 1
            p = p.next
        return dummpy.next