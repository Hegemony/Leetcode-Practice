# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummpy = ListNode(' ')
        p = head
        cnt = 0
        while p:
            cnt += 1
            p = p.next
        p = head
        res = 0
        while p:
            res += 1
            if res == cnt - k + 1:
                dummpy.next = p
                break
            p = p.next
        return dummpy.next