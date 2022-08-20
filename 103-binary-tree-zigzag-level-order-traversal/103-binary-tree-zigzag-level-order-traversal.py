# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque([root])
        res = []
        ltor = False
        while q:
            l = len(q)
            res.append([])
            if ltor:
                for _ in range(l):
                    popped = q.popleft()
                    res[-1].append(popped.val)
                    if popped.right:
                        q.append(popped.right)
                    if popped.left:
                        q.append(popped.left)
            else:
                for _ in range(l):
                    popped = q.pop()
                    res[-1].append(popped.val)
                    if popped.left:
                        q.appendleft(popped.left)
                    if popped.right:
                        q.appendleft(popped.right)
            ltor = not ltor
        return res
                
        