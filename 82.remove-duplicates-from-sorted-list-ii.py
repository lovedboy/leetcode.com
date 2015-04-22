#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        
        if not head:
            return

        pre = None
        cur = head

        while cur and cur.next:

            if cur.val == cur.next.val:

                val = cur.val

                while cur and cur.val == val:
                    cur = cur.next
                
                if pre is None:
                    return self.deleteDuplicates(cur)
                else:
                    pre.next = self.deleteDuplicates(cur)
            else:
                if pre is None:
                    head = cur
            
                pre = cur
                
            if cur:
                cur = cur.next

        return head