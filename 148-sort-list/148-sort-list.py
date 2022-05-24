# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp1 = head
        while temp1.next and temp1.next.next:
            temp1 = temp1.next.next
        if temp1.next:
            temp1 = temp1.next

        return self.mergeSortList(head, temp1)
    
    def mergeSortList(self, head, tail):
        if head == tail:
            temp1 = ListNode(head.val)
            return temp1

        temp1 = head
        temp2 = head
        while temp2 != tail and temp2.next != tail:
            temp1 = temp1.next
            temp2 = temp2.next.next
            
        left = self.mergeSortList(head, temp1)
        right = self.mergeSortList(temp1.next, tail)
        
        temp3 = ListNode()
        sortedHead = temp3
        
        while left and right:
            if left.val > right.val:
                temp3.val = right.val
                right = right.next
            else:
                temp3.val = left.val
                left = left.next
            temp3.next = ListNode()
            temp3 = temp3.next
        
        if right:
            temp3.val = right.val
            temp1 = right.next
        else:
            temp3.val = left.val
            temp1 = left.next
        
        while temp1:
            temp3.next = ListNode()
            temp3 = temp3.next
            temp3.val = temp1.val
            temp1 = temp1.next
        
        return sortedHead
            