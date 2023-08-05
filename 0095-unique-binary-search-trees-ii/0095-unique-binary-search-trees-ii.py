# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [ [None] * (n+1) for _ in range(n+1)]
        def solve(l, r):
            if l == r:
                return [TreeNode(l)]
            if l > r:
                return [None]
            if dp[l][r]:
                return dp[l][r]
            
            res = []
            for i in range(l, r+1):
                left = solve(l, i-1)
                right = solve(i+1, r)
                for l_node in left:
                    for r_node in right:
                        res.append(TreeNode(i, l_node, r_node))
            
            dp[l][r] = res
            return res
        
        return solve(1, n)