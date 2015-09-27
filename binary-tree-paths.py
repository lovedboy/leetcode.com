# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if not root:
            return result
        stack = [(root, [str(root.val)])]
        while stack:
            node, path = stack.pop(0)
            if node.left is None and node.right is None:
                result.append("->".join(path))
            if node.left:
                stack.append((node.left, path + [str(node.left.val)]))
            if node.right:
                stack.append((node.right, path + [str(node.right.val)]))
        
        return result
                

# class Solution(object):
#     def binaryTreePaths(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[str]
#         """
#         self.result = []
#         if not root:
#             return []
#         self.findPath(root, str(root.val))
#         return self.result
    
#     def findPath(self, node, path):
#         if node.left is None and node.right is None:
#             self.result.append(path)
#         if node.left:
#             self.findPath(node.left, path+"->{}".format(node.left.val))
#         if node.right:
#             self.findPath(node.right, path+"->{}".format(node.right.val))
        