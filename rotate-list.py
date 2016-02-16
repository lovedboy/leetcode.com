# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head is None:
            return head
        
        p1 = p2 = head
        n = 0
        while n < k and p2:
            p2 = p2.next
            n += 1
        
        if p2 is None:
            return self.rotateRight(head, k % n)
            
        new_head = None
        while p2 and p2.next:
            p1 ,p2 = p1.next, p2.next
            
        new_head = p1.next
            
        p2.next = head
        p1.next = None
        
        return new_head
            
            
        