# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        part_len = length//k
        remainder = length % k
        res = []
        temp = head
        while temp or k:
            temp_head = ListNode()
            pointer = temp_head
            for _ in range(part_len + int(remainder > 0)):
                if not temp:
                    break
                    
                pointer.next = temp
                pointer = pointer.next
                temp = temp.next
            
            pointer.next = None
            res.append(temp_head.next)
            
            remainder -= 1
            k -= 1
        
        return res