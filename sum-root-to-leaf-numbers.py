# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if not root:
            return sum
        stack = [(root, root.val)]
        while stack:
            node, result = stack.pop()
            if node.left:
                stack.append((node.left, result*10 + node.left.val))
            if node.right:
                stack.append((node.right, result*10 + node.right.val))
            if node.left is None and node.right is None:
                sum += result
        return sum
        