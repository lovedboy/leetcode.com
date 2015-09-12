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
            tmp = []
            for node in leaf:
                node.left, node.right = node.right, node.left
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            leaf = tmp

        return root

