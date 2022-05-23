# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp1 = head.next
        temp2 = head.next
        stack = [head.val]
        while temp2 and temp2.next:
            stack.append(temp1.val)
            temp1 = temp1.next
            temp2 = temp2.next.next
            
        maxSum = -1
        while temp1:
            maxSum = max(maxSum, stack.pop()+temp1.val)
            temp1 = temp1.next
            
        return maxSum