# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        cur = head
        great = great_head = ListNode(0)
        less = less_head = ListNode(0)
        while cur:
            if cur.val >= x:
                great.next, cur = cur, cur.next
                great = great.next
                great.next = None
            else:
                less.next, cur = cur, cur.next
                less = less.next
                less.next = None
                
        less.next = great_head.next
        return less_head.next