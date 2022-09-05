"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque([root])
        res = []
        while q:
            l = len(q)
            res.append([])
            for _ in range(l):
                popped = q.popleft()
                res[-1].append(popped.val)
                for child in popped.children:
                    q.append(child)
        return res