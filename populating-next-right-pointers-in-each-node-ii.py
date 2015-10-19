# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        depth = 0
        stack = [(root, depth)]
        nodes = []
        while stack:
            node, dp = stack.pop(0)
            if dp == depth:
                nodes.append(node)
            else:
                self.giveNextNodes(nodes)
                nodes = [node]
                depth += 1
            if node.left:
                stack.append((node.left, dp + 1))
            if node.right:
                stack.append((node.right, dp + 1))
                
        self.giveNextNodes(nodes)
    
    def giveNextNodes(self, nodes):
        for i in xrange(0, len(nodes) - 1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = None
            
        