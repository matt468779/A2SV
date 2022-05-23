# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp = head.next
        prev2 = head
        while temp != None:
            prev = None
            temp2 = head
            temp3 = temp.next
            swapped = False
            while temp2 != temp:
                if temp2.val >= temp.val:
                    if prev != None:
                        prev.next = temp
                        temp.next = temp2
                    else:
                        temp.next = head
                        head = temp
                    prev2.next = temp3
                    swapped = True
                    break
                prev = temp2
                temp2 = temp2.next
            if swapped == False:
                prev2 = prev2.next
            temp = temp3
        return head