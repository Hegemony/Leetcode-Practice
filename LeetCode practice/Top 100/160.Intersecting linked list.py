# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
题目要求返回结点，不是返回结点的值
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa = headA
        listA = []
        while pa != None:
            listA.append(pa.val)
            pa = pa.next

        pb = headB
        listB = []
        while pb != None:
            listB.append(pb.val)
            pb = pb.next

        for i in listB:
            if i in listA:
                return i

        return None

# a = [1, 2, 3, 4]
# b = [2, 3]
# for i in a:
#     if i in b:
#         print('t')
#     else:
#         print('f')


"""
题解：将结点存入集合中，返回集合中的结点。
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        res = set()
        pa = headA
        while pa != None:
            res.add(pa)
            pa = pa.next

        pb = headB
        while pb != None:
            if pb in res:
                return pb
            else:
                res.add(pb)
            pb = pb.next

        return None

