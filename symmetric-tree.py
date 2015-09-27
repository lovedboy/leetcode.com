# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
        if not root:
            return True
        
        depth = 1
        nodes = []
        stack = [(root, depth)]
        while stack:
            node, d = stack.pop(0)
            if d == depth:
                nodes.append(node.val if node else None)
            else:
                if self.checkNodes(nodes) is False:
                    return False
                nodes = [node.val] if node else [None]
                depth += 1
            if node:
                stack.append((node.left, d+1))
                stack.append((node.right, d+1))
        
        return self.checkNodes(nodes)
    
    def checkNodes(self, nodes):
        length = len(nodes)
        for i in range(0, length / 2):
            if nodes[i] != nodes[length - 1 - i]:
                return False
        return True
                
            
# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
    
#         if not root:
#             return True
        
#         return self.checkSame(root.left, root.right)
        
#     def checkSame(self, left, right):
            
#         if left is None and right is None:
#             return True
#         if left is None or right is None:
#             return False
#         if left.val != right.val:
#             return False
#         return self.checkSame(left.left, right.right) and self.checkSame(left.right, right.left)
#             