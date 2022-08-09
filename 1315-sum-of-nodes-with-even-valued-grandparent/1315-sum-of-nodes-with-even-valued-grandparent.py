# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
        def sumEven(root: TreeNode, parent: TreeNode, gParent: TreeNode):
            if root:
                if gParent and not gParent.val % 2:
                    self.res += root.val
                sumEven(root.left, root, parent)
                sumEven(root.right, root, parent)
        sumEven(root, None, None)
        return self.res