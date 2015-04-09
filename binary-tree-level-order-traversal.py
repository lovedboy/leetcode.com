# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):

        val_list = []
        node_list = []

        if root is None:
            return val_list

        node_list.append(root)

        while node_list:

            _val_list = []
            _node_list = []

            for node in node_list:
                _val_list.append(node.val)
                if node.left:
                    _node_list.append(node.left)

                if node.right:
                    _node_list.append(node.right)

            val_list.append(_val_list)

            node_list = _node_list

        return val_list
            