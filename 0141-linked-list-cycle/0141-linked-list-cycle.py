# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow, fast = head, head.next
        while fast != None and slow != fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        if fast == None:
            return False
        return True