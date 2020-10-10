# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return
        p = head
        res = []
        while p:
            res.append(p.val)
            p = p.next
        res.reverse()
        head = ListNode(res[0])
        q = head
        for i in range(1, len(res)):
            newnode = ListNode(res[i])
            q.next = newnode
            q = q.next

        return head


"""
题解双指针写法
"""

class Solution:
    # 双指针，一个指针用作新生成的一个链表当前节点，另一个指针用于源链表遍历
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre = head
        cur = None
        while pre:
            # 这个临时节点就相当于一个副本
            temp = ListNode(pre.val)
            temp.next = cur
            cur = temp
            pre = pre.next
        return cur
