# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        cur = head
        pre = new_head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre.next  = cur
                pre = cur
            cur = cur.next
        return new_head.next
                