# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
            
        if head.next is None:
            return TreeNode(head.val)
            
        p1 = p2 = head
        pre = None
        while p2 and p2.next:
            p2 = p2.next.next
            pre ,p1 = p1, p1.next
        
        root = TreeNode(p1.val)
        root.right = self.sortedListToBST(p1.next)
        pre.next = None
        root.left = self.sortedListToBST(head)
        return root
        
        