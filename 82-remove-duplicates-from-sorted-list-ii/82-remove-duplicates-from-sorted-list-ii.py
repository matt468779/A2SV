# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        pointHead = ListNode(0, head)
        same = -101
        temp1 = head
        temp2 = pointHead
            
        while temp1.next and temp1.next.next:
            if temp1.val == temp1.next.val:
                same = temp1.val
                temp2.next = temp1.next.next
                temp1 = temp1.next.next
            elif same == temp1.val and temp1.next.val == temp1.next.next.val:
                temp2.next = temp1.next
                temp1 = temp1.next
            elif same == temp1.val and temp1.next.val != temp1.next.next.val:
                temp2.next = temp1.next
                temp2 = temp2.next
                temp1 = temp1.next.next
            elif same != temp1.val and temp1.next.val != temp1.next.next.val:
                temp2 = temp2.next.next
                temp1 = temp1.next.next                
            else:
                temp2 = temp2.next
                temp1 = temp1.next

        if temp1 and temp1.val == same:
            temp2.next = temp1.next
        if temp1 and temp1.next and (temp1.next.val == same or temp1.val == temp1.next.val):
            temp2.next = temp1.next.next

        
                            
        return pointHead.next