# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, res = stack.pop()
            if node.right:
                stack.append((node.right, res+node.right.val))
            if node.left:
                stack.append((node.left, res+node.left.val))
            if node.right is None and node.left is None:
                if res == sum:
                    return True
        return False
        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def hasPathSum(self, root, sum):
#         """
#         :type root: TreeNode
#         :type sum: int
#         :rtype: bool
#         """
#         if not root:
#             return False
    
#         if root.left is None and root.right is None:
#             return root.val == sum
        
#         return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
#         