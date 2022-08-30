# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.preSum = [0]
        def dfs1(node):
            if node:
                dfs1(node.right)
                self.preSum.append(self.preSum[-1]+node.val)
                dfs1(node.left)
        
        def dfs2(node):
            if node:
                dfs2(node.left)
                node.val = self.preSum.pop()
                dfs2(node.right)
                
        dfs1(root)
        dfs2(root)
        return root