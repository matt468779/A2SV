# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([(root, 0)])
        res = collections.deque([])
        mi, mx = float('inf'), 0
        while q:
            l = len(q)
            for _ in range(l):
                popped = q.popleft()
                if popped[1] < mi:
                    res.appendleft([[popped[0].val]])
                    mi = popped[1]
                elif popped[1] > mx:
                    res.append([[popped[0].val]])
                    mx = popped[1]
                else:
                    if type(res[popped[1] - mi][-1]) is list:
                        res[popped[1] - mi][-1].append(popped[0].val)
                    else:
                        res[popped[1] - mi].append([popped[0].val])
                if popped[0].left:
                    q.append((popped[0].left, popped[1]-1))
                if popped[0].right:
                    q.append((popped[0].right, popped[1]+1))
            print(res)
            for i in range(len(res)):
                if type(res[i][-1]) is list:
                    res[i].extend(sorted(res[i].pop()))
        return res