
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):

        if head is None:
            return

        p = head
        new_head = ListNode(head.val)
        new_head.next = None

        while p.next:

            p = p.next
            pre = None
            cur = new_head

            while cur and cur.val < p.val:
                pre = cur
                cur = cur.next

            t = ListNode(p.val)

            if pre is None:
                new_head = t
                t.next = cur

            else:
                pre.next = t
                t.next = cur

        return new_head


def print_link_list(head):

    while head:
        
        print head.val

        head = head.next


a1 = ListNode(1)
a2 = ListNode(1)
a1.next = a2

t = Solution().insertionSortList(a1)

print_link_list(t)