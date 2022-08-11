# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.wrong = []
        self.lastSeen = TreeNode(float(-inf))
        
        def dfs(node):
            if node:
                dfs(node.left)

                if not self.wrong and self.lastSeen.val > node.val:
                    self.wrong.append(self.lastSeen)
                    self.wrong.append(node)
                    self.lastSeen = node
                elif self.wrong and self.lastSeen.val > node.val:
                    self.wrong.append(node)
                elif node.val >= self.lastSeen.val:
                    self.lastSeen = node
                    
                dfs(node.right)
                
        dfs(root)
        
        if len(self.wrong) > 2:
            self.wrong[0].val, self.wrong[-1].val = self.wrong[-1].val, self.wrong[0].val
        else:
            self.wrong[0].val, self.wrong[1].val = self.wrong[1].val, self.wrong[0].val