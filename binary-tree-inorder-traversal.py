# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        p = root
        stack = []
        result = []
        while ( p or stack):
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop(-1)
                result.append(p.val)
                p = p.right
        return result
                