# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        last = head
        while last.next != None:
            last = last.next
            middle = middle.next
            if last.next == None:
                break
            last = last.next
        return middle