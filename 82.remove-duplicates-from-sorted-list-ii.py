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

        while cur:

            if cur.next and cur.val == cur.next.val:

                val = cur.val

                while cur and cur.val != val:
                    cur = cur.next

            if pre is None:
                pre = cur
                head = cur
            else:
                pre.next = cur

            if cur:
                cur = cur.next

        return head