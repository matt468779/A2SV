# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = res = ListNode(0, head)
        count = 0
        while temp and count <= right:
            if count == left-1:
                middle_start = temp
                temp = temp.next
            elif count == left:
                middle = middle_end = temp
                temp = temp.next
            elif left < count <= right:
                temp_next = temp.next
                temp.next = middle
                middle = temp
                temp = temp_next
            else:
                temp = temp.next
            
            count += 1
            
        middle_start.next = middle
        middle_end.next = temp
        return res.next