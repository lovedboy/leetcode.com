# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        # print left_depth, right_depth
        if abs(left_depth - right_depth) >1:
            return False
        return  self.isBalanced(root.left) and self.isBalanced(root.right)
   
    def depth(self, root):
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 1
        while stack:
            node, d = stack.pop(0)
            if node.left is None and node.right is None:
                max_depth = d
            if node.left:
                stack.append((node.left, d+1))
            if node.right:
                stack.append((node.right, d+1))
        return max_depth
                
            
         