"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dict = {}
        temp = head
        temp_res = res = Node(0)
        while temp:
            temp_res.next = Node(temp.val)
            node_dict[temp] = temp_res.next
            temp_res = temp_res.next
            temp = temp.next
        
        temp = head
        temp_res = res.next
        while temp:
            if temp.random:
                temp_res.random = node_dict[temp.random]
            temp_res = temp_res.next
            temp = temp.next
        
        return res.next