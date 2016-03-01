# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        node = root
        stack = []
        last_visit_node = None
        value = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                test_node = stack[-1]
                if test_node.right and last_visit_node != test_node.right:
                    node = test_node.right
                else:
                    last_visit_node = test_node
                    value.append(test_node.val)
                    stack.pop(-1)
        return value
        