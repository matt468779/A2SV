# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        childs = set()

        for node in descriptions:
            if node[0] not in nodes:
                nodes[node[0]] = TreeNode(node[0])
            if node[1] not in nodes:
                nodes[node[1]] = TreeNode(node[1])
            
            if node[2]:
                nodes[node[0]].left = nodes[node[1]]
            else:
                nodes[node[0]].right = nodes[node[1]]
            
            childs.add(node[1])            
        
        root = None
        for node in descriptions:
            if node[0] not in childs:
                root = nodes[node[0]]
                break
                
        return root