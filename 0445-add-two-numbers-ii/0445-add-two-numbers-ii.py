# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNum(root):
            num = 0
            while root:
                num = num*10 + root.val
                root = root.next
            
            return num
        
        def toLinkedList(num):
            if num == 0:
                return ListNode()
            
            res = None
            while num:
                temp = ListNode(num % 10)
                temp.next = res
                res = temp
                num //= 10
            
            return res
        
        res = getNum(l1) + getNum(l2)
        return toLinkedList(res)
        