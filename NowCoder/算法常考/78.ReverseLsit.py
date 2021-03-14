# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        cur, pre = None, None
        p = pHead
        while p:
            pre = p.next
            p.next = cur
            cur = p
            p = pre
        return cur