# Runtime: 52 ms, faster than 81.26% of Python3 online submissions for Find Bottom Left Tree Value.
# Memory Usage: 16.2 MB, less than 21.44% of Python3 online submissions for Find Bottom Left Tree Value.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.node_val = []
        self.layer_list = []
        self.traverse(root, 0)
        # return first occurrence with max depth
        return self.node_val[self.layer_list.index(max(self.layer_list))] 
        
    def traverse(self, node, layer):
        if not node: return
        layer = layer + 1
        self.node_val.append(node.val)
        self.layer_list.append(layer)
        self.traverse(node.left, layer)
        self.traverse(node.right, layer)
