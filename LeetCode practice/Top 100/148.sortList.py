# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(left, right):
            h = res = ListNode(0)
            while left and right:
                if left.val < right.val:
                    h.next = left
                    left = left.next
                else:
                    h.next = right
                    right = right.next
                h = h.next

            # while left:
            #     h.next = left
            #     left = left.next
            #     h = h.next
            # while right:
            #     h.next = right
            #     right = right.next
            #     h = h.next
            h.next = left if left else right
            return res.next

        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next  # 从mid切开，保存后面的半段
        slow.next = None  # 将前面断开
        left, right = self.sortList(head), self.sortList(mid)
        return merge(left, right)


"""
归并排序
"""


class Solution1:
    def merge(self, left, right):
        res = []
        len1 = len(left)
        len2 = len(right)
        i, j = 0, 0
        while i < len1 and j < len2:
            if left[i] > right[j]:
                res.append(right[j])
                j += 1
            else:
                res.append(left[i])
                i += 1
        print('*', res, left[i + 1:], right[j + 1:])

        # while i < len1:
        #     res.append(left[i])
        #     i += 1
        # while j < len2:
        #     res.append(right[j])
        #     j += 1

        res += left[i:] if left[i:] else right[j:]
        print(res)
        return res

    def merge_sort(self, a):
        l = len(a)
        if l <= 1:
            return a
        mid = l // 2
        left = self.merge_sort(a[:mid])
        right = self.merge_sort(a[mid:])
        return self.merge(left, right)


print(Solution1().merge_sort([3, 2, 1, 5, 6, 4]))
