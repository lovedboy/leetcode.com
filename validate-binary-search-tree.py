# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        p = root
        stack = []
        val = []
        
        while p or stack:
            
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop(-1)
                val.append(p.val)
                p = p.right
                
        for i in range(0, len(val) - 1):
            if val[i] >= val[i+1]:
                return False
        
        return True
        