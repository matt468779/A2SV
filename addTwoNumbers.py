# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode()
        l3Root = l3
        carry = 0

        while True:
            sum = l1.val + l2.val + carry
            
            l3.val = sum % 10
            if (sum >= 10):
                carry = 1
            else:
                carry = 0
            print ("--", end='')
            print (l3.val)
            l1 = l1.next
            l2 = l2.next
            if l1 == None or l2 == None:
                break
            l3.next = ListNode()
            l3 = l3.next
        big = None
        if l1 == None and l2 == None:
            if carry == 1:
                l3.next = ListNode()
                l3.next.val = 1
            return l3Root
        elif l1 == None:
            big = l2
        else:
            big = l1
        
        while True:
            sum = big.val + carry
            l3.next = ListNode()
            l3 = l3.next
            l3.val = sum % 10
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            big = big.next
            if big == None:
                break
            
        if carry == 1:
            l3.next = ListNode()
            l3.next.val = 1
        
        return l3Root
    

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
def displayList(list):
    while list != None:
        print (list.val, end='')
        print (" ", end='')
        list = list.next

if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(9)
    l2 = ListNode(9, ListNode(9, ListNode(9)))
    

    
    displayList(l1)
    print ("hello")
    displayList(l2)

    l3 = sol.addTwoNumbers(l1, l2)
    print (l3.val)
    displayList(l3)
