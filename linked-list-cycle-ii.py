'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        
        if not head:
            return

        m = head
        n = head

        while m and m.next and n and n.next and n.next.next:
            m = m.next
            n = n.next.next

            if m is n:
                return m

        return