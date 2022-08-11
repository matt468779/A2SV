# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if node:
                depthLeft = dfs(node.left, depth+1)
                depthRight = dfs(node.right, depth+1)
                if depthLeft == depthRight and depthLeft >= self.maxDepth:
                    self.maxDepth = depthLeft
                    self.lca = node
                    return depthLeft
                else:
                    return max(depthLeft, depthRight)              
            return depth
        
        self.maxDepth = 0
        dfs(root, 0)
        return self.lca