# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None or head.next is None:
            return True

        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast is not None:
            slow = slow.next

        slow = self.reverse(slow)

        while slow:
            if slow.val != head.val:
                break
            slow = slow.next
            head = head.next
            
        return slow is None

    def reverse(self, head):

        if head is None:
            return head

        pre = next = None

        while head:
            
            next = head.next
            head.next = pre
            pre = head
            head = next

        return pre

