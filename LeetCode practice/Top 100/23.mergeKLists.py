# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        import heapq
        res = []  # 建立堆，存储每个链表的最小值，用于比较
        dummy = ListNode(0)
        p = dummy
        for i in range(len(lists)):
            if lists[i]:  # lists中存储的是每个链表的头节点
                heapq.heappush(res, (lists[i].val, i))
                lists[i] = lists[i].next
        while res:
            val, idx = heapq.heappop(res)
            p.next = ListNode(val)
            if lists[idx]:  # lists中存储的是每个链表的头节点
                heapq.heappush(res, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
            p = p.next
        return dummy.next