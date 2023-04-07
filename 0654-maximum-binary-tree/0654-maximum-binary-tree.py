# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:        
        def solve(l, r):
            if l > r:
                return None
            
            maxInd = l
            for i in range(l+1, r+1):
                if nums[i] > nums[maxInd]:
                    maxInd = i
                    
            return TreeNode(nums[maxInd], solve(l, maxInd-1), solve(maxInd+1, r))
            
        return solve(0, len(nums)-1)