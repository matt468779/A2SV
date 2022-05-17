# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp1 = head
        temp2 = head.next
        temp3 = head.next.next
        head.next = None
        while temp2.next != None:
            temp2.next = temp1
            temp1 = temp2
            temp2 = temp3
            temp3 = temp2.next

        temp2.next = temp1
        
        return temp2
            