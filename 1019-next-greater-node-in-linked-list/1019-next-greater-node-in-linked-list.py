# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp = head
        res = []
        stack = []
        i = 0
        while temp != None:
            res.append(0)
            count = 0
            while stack and stack[-1] < temp.val:
                stack.pop()
                count += 1
            stack.append(temp.val)
            
            j = i-1
            while count > 0 and j >= 0:
                if res[j] == 0:
                    res[j] = temp.val
                    count -= 1
                j -= 1
            temp = temp.next
            i += 1
        return res