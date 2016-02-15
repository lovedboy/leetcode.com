# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = None
        p1 = p2 = head
        while n>0:
            p2 = p2.next
            n -= 1

        while p2:
            p2 = p2.next
            pre, p1 = p1, p1.next

        if pre is None:
            return head.next
        else:
            pre.next = p1.next
            return head


