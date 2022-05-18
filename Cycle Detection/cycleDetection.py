# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    if head == None or head.next == None:
        return 0
    temp1 = head
    temp2 = head.next
    while temp2 != None:
        if temp1 == temp2:
            return 1
        temp1 = temp1.next
        temp2 = temp2.next
        if temp2 != None:
            temp2 = temp2.next
    return 0
