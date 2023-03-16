# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        def merge(node1, node2):
            res = ListNode()
            result = res
            while node1 and node2:
                if node1.val < node2.val:
                    res.next = ListNode(node1.val)
                    node1 = node1.next
                else:
                    res.next = ListNode(node2.val)
                    node2 = node2.next
                res = res.next
            res.next = node1 or node2
            return result.next
            
        def merge_sort(start, end):
            if start == end:
                return ListNode(start.val)
                            
            slow = start
            fast = start
            while fast.next != end:
                slow = slow.next
                fast = fast.next
                if fast.next != end:
                    fast = fast.next
            
            
            node1 = merge_sort(start, slow)
            node2 = merge_sort(slow.next, end)
            
            return merge(node1, node2)
        
        
        end = head
        while end.next:
            end = end.next
        
        return merge_sort(head, end)