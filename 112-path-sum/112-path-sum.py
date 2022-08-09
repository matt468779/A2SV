# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSum = targetSum
        self.res = False
        self.hasPathSumHelper(root, 0)
        return self.res
    
    def hasPathSumHelper(self, root: Optional[TreeNode], sumSoFar: int) -> bool:
        if root and not self.res:
            self.hasPathSumHelper(root.left, sumSoFar+root.val)
            self.hasPathSumHelper(root.right, sumSoFar+root.val)
            if not root.left and not root.right:
                if sumSoFar + root.val == self.targetSum:
                    self.res = True