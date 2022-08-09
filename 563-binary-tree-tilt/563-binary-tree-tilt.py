# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def findTilt(self, root:Optional[TreeNode]) -> int:
        self.sum = 0
        self.findTiltHelper(root)
        return self.sum
    def findTiltHelper(self, root: Optional[TreeNode]) -> int:
        if root:
            leftSum = self.findTiltHelper(root.left)
            rightSum = self.findTiltHelper(root.right)
            res = leftSum - rightSum
            self.sum += res if res > 0 else -res
            
            return root.val + leftSum + rightSum
        else:
            return 0