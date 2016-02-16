# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import sys
sys.setrecursionlimit(10000)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
           return lists[0]
           
        mid = len(lists) / 2
        head1 = self.mergeKLists(lists[0:mid])
        head2 = self.mergeKLists(lists[mid:])
        return self.merge(head1,head2)
            
            
    def merge(self, head1,head2):
            
            p = head = ListNode(0)
            p1 = head1
            p2 = head2
            while p1 and p2:
                if p1.val < p2.val:
                    p.next, p1 = p1, p1.next
                else:
                    p.next, p2 = p2, p2.next
                p = p.next
                
            while p1:
                p.next, p1 = p1, p1.next
                p = p.next
                
            while p2:
                p.next, p2 = p2, p2.next
                p = p.next
            
            return head.next               
                    
        