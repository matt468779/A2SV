# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        
        merged = ListNode()
        head = merged
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                merged.val = list1.val
                list1 = list1.next
            else:
                merged.val = list2.val
                list2 = list2.next
            merged.next = ListNode()
            merged = merged.next
            
        if list1 == None:
            merged.val = list2.val
            merged.next = list2.next
        else:
            merged.val = list1.val
            merged.next = list1.next
        return head