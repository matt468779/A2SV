# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            temp = lists[i]
            while temp != None:
                heapq.heappush(heap, temp.val)
                temp = temp.next
                
        head = ListNode()
        temp = head
        while len(heap) > 0:
            temp.next = ListNode(heapq.heappop(heap))
            temp = temp.next
            
        return head.next