# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        self.selectPath(root, [], sum, result)
        return result
    
    
    def selectPath(self, root, path, sum, result):
        if root.left is None and root.right is None:
            if sum == root.val:
                result.append(path + [root.val] )
        if root.left:
            self.selectPath(root.left, path + [root.val], sum - root.val , result)
        if root.right:
            self.selectPath(root.right, path + [root.val], sum - root.val , result)
            
        
        