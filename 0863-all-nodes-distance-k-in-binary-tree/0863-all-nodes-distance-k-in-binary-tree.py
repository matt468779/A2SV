# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:        
        res = []
        parent = {}
        q = deque([root])
        while q:
            l = len(q)
            for _ in range(l):
                popped = q.popleft()
                if popped.left:
                    parent[popped.left.val] = popped
                    q.append(popped.left)
                    
                if popped.right:
                    parent[popped.right.val] = popped
                    q.append(popped.right)
                
        visited = set()
        def solve(node, length):
            if not node or node.val in visited:
                return
            
            if length == k:
                res.append(node.val)
                return
            
            visited.add(node.val)
            
            solve(node.left, length+1)
            solve(node.right, length+1)
            solve(parent.get(node.val, None), length+1)
        
        solve(target, 0)
        
        return res