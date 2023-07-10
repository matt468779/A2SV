# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 1
        q = deque([root])
        while q:
            l = len(q)
            for _ in range(l):
                popped = q.popleft()
                if not popped.left and not popped.right:
                    return res
                
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                    
            res += 1
        
        return res-1