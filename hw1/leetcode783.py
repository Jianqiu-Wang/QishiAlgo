"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
"""
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.min_diff = float("inf")
        self.temp_max = -float("inf") # maxinum val in current branch except root
        
        def inorder_traversal(node):
            """ 
            """
            if not node: return
            inorder_traversal(node.left) # temp max will be updated
            self.min_diff = min(self.min_diff, node.val-self.temp_max)
            self.temp_max = node.val # update temp_max
            inorder_traversal(node.right)
            
        inorder_traversal(root)
        return self.min_diff