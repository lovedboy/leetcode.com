# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        
        place = ListNode(0)
        place.next = head
        pre = place
        cur = head
        while cur and cur.next:
            
            node1 = cur
            node2 = cur.next
            cur = cur.next.next if cur.next else None
            # swap
            pre.next = node2
            node2.next = node1
            node1.next = None
            pre = node1
        if cur:
            pre.next = cur
            
        return place.next
            
            
        