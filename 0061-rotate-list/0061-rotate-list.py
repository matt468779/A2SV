# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        tail = head
        length = 1
        while tail.next:
            length += 1
            tail = tail.next
        
        k %= length
        
        if k == 0:
            return head
        
        temp = head
        for _ in range(length-k-1):
            temp = temp.next
        
        temp_head = temp.next
        temp.next = None
        tail.next = head
        
        return temp_head
        
        