# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, mx):
            if node:
                if node.val >= mx:
                    self.res += 1
                    mx = node.val
                dfs(node.left, mx)
                dfs(node.right, mx)
                
        dfs(root, float(-inf))
        return self.res