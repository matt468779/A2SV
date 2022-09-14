# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, pali):
            if node:
                if pali.get(node.val):
                    if pali[node.val] > 1:
                        pali[node.val] -= 1
                    else:
                        pali.pop(node.val)
                else:
                    pali[node.val] = 1
                
                if node.left and node.right:
                    dfs(node.left, pali.copy())
                    dfs(node.right, pali.copy())
                elif node.left:
                    dfs(node.left, pali.copy())
                else:
                    dfs(node.right, pali.copy())
            elif len(pali) == 0 or (len(pali) == 1 and list(pali.items())[0][1] == 1):
                self.res += 1
        
        dfs(root, {})
        return self.res
        
            