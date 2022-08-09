"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        depth = 0
        q = collections.deque([root])
        while q:
            l = len(q)
            for i in range(l):
                children = q.popleft().children
                if children:
                    q.extend(children)
            depth += 1
            
        return depth
            
        