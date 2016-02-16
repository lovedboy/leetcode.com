# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return 

        pre = None
        p1 = p2 = p = head
        while p2 and p2.next:
            p2 = p2.next.next
            pre, p1 = p1, p1.next

        pre.next = None
        p1 = self.reverse(p1)
        while 1:
            p1_next = p1.next
            p_next = p.next
            if p_next is None:
                p.next = p1
                break
            p.next = p1
            p1.next = p_next
            p = p_next
            p1 = p1_next


    def reverse(self,head):
        
        pre = None
        cur = head
        next = None

        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre