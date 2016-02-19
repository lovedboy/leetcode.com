# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        m = max(p.val,q.val)
        n = min(p.val,q.val)
        if root.val > m:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < n:
            return self.lowestCommonAncestor(root.right, p, q)
        if n < root.val < m:
            return root
        if root.val == m or root.val == n:
            return root
            
        