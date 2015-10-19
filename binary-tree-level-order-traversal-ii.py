# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        stack = [(root, 0)]
        depth = 0
        vals = []
        while stack:
            node,d = stack.pop(0)
            if d != depth:
                result.insert(0, vals)
                vals = [node.val]
                depth = d
            else:
                vals.append(node.val)
            
            if node.left:
                stack.append((node.left, d+1))
            if node.right:
                stack.append((node.right, d+1))
                
        if vals:
            result.insert(0, vals)
        
        return result
        
        