
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):

        if not head:
            return

        pre = None
        cur = head

        while cur:
            
            if pre and pre.val == cur.val:
                cur = cur.next
                pre.next = cur

            else:
                pre = cur
                cur = cur.next

        return head
