# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessthan = ListNode()
        greater_or_equal = ListNode()
        temp_lessthan = lessthan
        temp_greater = greater_or_equal
        temp = head
        while temp:
            if temp.val >= x:
                greater_or_equal.next = temp
                greater_or_equal = temp
                temp = temp.next
                greater_or_equal.next = None
            else:
                lessthan.next = temp
                lessthan = temp
                temp = temp.next
                lessthan.next = None
        
        lessthan.next = temp_greater.next
        return temp_lessthan.next