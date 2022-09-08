# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node:
                dfs(node.left)
                self.res.append(node.val)
                dfs(node.right)
        self.res = []
        dfs(root)
        return self.res