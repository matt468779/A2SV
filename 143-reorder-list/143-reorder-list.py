# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return
        temp1 = head
        temp2 = head
        while temp2 and temp2.next:
            temp1 = temp1.next
            temp2 = temp2.next.next
        if temp2:
            temp1 = temp1.next
            
        stack = [temp1]
        while temp1.next:
            stack.append(temp1.next)
            temp1 = temp1.next
            
        while stack:
            temp1 = head.next
            head.next = stack.pop()
            head.next.next = temp1
            head = temp1
        head.next = None
        
        
    
        
        
        