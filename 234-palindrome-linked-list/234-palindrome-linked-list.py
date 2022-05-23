# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp1 = head
        temp2 = head
        stack = []
        while temp2 and temp2.next:
            stack.append(temp1.val)
            temp1 = temp1.next
            temp2 = temp2.next.next
            
        if temp2:
            temp1 = temp1.next

        while temp1:
            if temp1.val != stack.pop():
                return False
            temp1 = temp1.next

        return True
        