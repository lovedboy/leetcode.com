# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        if p1 is None or p2 is None:
            return None
        if id(p1) == id(p2):
            return p1
            
        l1 = 0
        while p1:
            p1 = p1.next
            l1 += 1
            
        l2 = 0
        while p2:
            p2 = p2.next
            l2 += 1
            
        s1 = headA
        s2 = headB
        
        if l1 > l2:
            l = l1 - l2
            while l > 0:
                s1 = s1.next
                l -=1
                
        if l1 < l2:
            l = l2 - l1
            while l > 0:
                s2 = s2.next
                l -= 1
        
        while s1 and s2:
            if id(s1) == id(s2):
                return s1
            s1 = s1.next
            s2 = s2.next
        
        return None
                
                
        
        
        
        
        