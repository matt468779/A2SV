# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        while q:
            l = len(q)
            for _ in range(l):
                popped = q.popleft()
                if popped:
                    q.append(popped.left)
                    q.append(popped.right)
                    
            if len(q) % 2 == 1:
                return False
            for i in range(len(q)//2):
                if q[i] and q[len(q)-i-1] and q[i].val != q[len(q)-i-1].val:
                    return False
                elif (q[i] or q[len(q)-i-1]) and (not q[i] or not q[len(q)-i-1]):
                    return False  
                
        return True
            