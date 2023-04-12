# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        swaps = 0
        while q:
            l = len(q)
            for i in range(l):
                popped = q.popleft()
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                        
            temp = [node.val for node in q]
            temp2 = temp.copy()
            temp.sort()
            valInd = {temp[i]:i for i in range(len(temp))}
            for i in range(len(temp)):
                while temp[i] != temp2[i]:
                    ind = valInd[temp2[i]]
                    temp2[i], temp2[ind] = temp2[ind], temp2[i]
                    swaps += 1
                    
        return swaps