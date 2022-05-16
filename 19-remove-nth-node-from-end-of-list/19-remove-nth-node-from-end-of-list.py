# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        rem = ListNode(-1, head)
        i = 0
        while temp != None:
            temp = temp.next
            if i >= n:
                rem = rem.next
            i += 1
            
        if rem.next == head:
            return rem.next.next
        elif rem.next.next == None:
            rem.next = None
        else:
            rem.next = rem.next.next
         
        return head