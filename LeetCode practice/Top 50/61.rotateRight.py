# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        p = head
        l = 0
        while p:
            p = p.next
            l += 1

        cnt = k % l
        if cnt == 0:
            return head
        q = head
        n = 1
        while q:
            if n == l - cnt:
                tmp = q.next
                q.next = None
                break
            q = q.next
            n += 1

        s = tmp
        while s and s.next:
            s = s.next
        s.next = head
        return tmp
