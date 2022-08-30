# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.preSum = 0
        def dfs1(node):
            if node:
                dfs1(node.right)
                self.preSum += node.val
                node.val = self.preSum
                dfs1(node.left)
                
        dfs1(root)
        return root