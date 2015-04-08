'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):

        
        if not head:
            return False

        m = head
        n = head

        while m and m.next and n and n.next and n.next.next:
            m = m.next
            n = n.next.next

            if m is n:
                return True

        return False

# a1 = ListNode(1)
# a2 = ListNode(2)
# a3 = ListNode(2)

# a1.next = a2
# a2.next = a3
# a3.next = a1

# print Solution().hasCycle(a1)