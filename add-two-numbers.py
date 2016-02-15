# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = p = ListNode(0)
        n = 0
        while l1 or l2 or n > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + n 
            n = s / 10 if s > 9 else 0
            p.next = ListNode( s % 10)
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return l.next