# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(hp, (lists[i].val, i))
                lists[i] = lists[i].next
        
        res = ListNode()
        temp = res
        while hp:
            val, i = heapq.heappop(hp)
            temp.next = ListNode(val)
            temp = temp.next
            if lists[i]:
                heapq.heappush(hp, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return res.next