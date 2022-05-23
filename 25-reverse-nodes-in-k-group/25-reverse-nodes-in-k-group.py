# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        temp = head
        temp2 = head
        finished = False
        prev = None
        while temp != None: 
            for _ in range(k-1):
                if temp2.next == None:
                    finished = True
                    break
                temp2 = temp2.next
            if not finished:                    
                if prev != None:
                    prev.next = self.reverse(temp, temp2.next, k)
                else:
                    self.reverse(temp, temp2.next, k)
                    head = temp2                
            else:
                break            
            prev = temp
            temp = temp.next
            temp2 = temp    
        return head
    
    def reverse(self, head: Optional[ListNode], last: Optional[ListNode], k):
        temp1 = head
        temp2 = head.next
        temp3 = head.next.next
        while temp3 != last:
            temp2.next = temp1
            temp1 = temp2
            temp2 = temp3
            temp3 = temp3.next
        temp2.next = temp1
        head.next = last
        return temp2