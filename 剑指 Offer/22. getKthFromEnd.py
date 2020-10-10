# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = head
        q = head
        res = 0
        while p.next != None:
            res += 1
            p = p.next
            if res >= k:
                q = q.next
        return q


"""
题解写法：比较简洁
"""
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter
