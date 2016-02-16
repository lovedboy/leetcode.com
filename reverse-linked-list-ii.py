# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
            
        new_head = ListNode(0)
        new_head.next = head
        k = 0
        p = new_head
        point = None
        while p and k <= m:
            if k == m:
                point.next = self.reverse(p, n-m)
                break
            else:
                point, p = p, p.next
            k += 1

        return new_head.next
    

    def reverse(self, head, n):

        if head is None:
            return head

        cur = p = head
        pre = None
        k = 0
        while k <= n and cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            k += 1
            
        p.next = cur
        return pre

