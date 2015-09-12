# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        leaf = [root]
        while leaf:
            node = leaf.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                leaf.append(node.left)
            if node.right:
                leaf.append(node.right)
        return root

