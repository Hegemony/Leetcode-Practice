# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p, q = head, head
        cnt = 0
        while q:
            if cnt < k:
                cnt += 1
                q = q.next
            else:
                p = p.next
                q = q.next
                print(p.val, q.val)
        return p


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
