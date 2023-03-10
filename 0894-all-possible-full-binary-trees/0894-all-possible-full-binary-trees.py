# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        memo = {1: [TreeNode()]}
        def solve(n):
            if n in memo:
                return memo[n]
            
            res = []
            for i in range(1, n-1, 2):
                left = solve(i)
                right = solve(n-i-1)
                for leftnode in left:
                    for rightnode in right:
                        root = TreeNode(left=leftnode, right=rightnode)
                        res.append(root)
            
            memo[n] = res
            return res
        
        return solve(n)