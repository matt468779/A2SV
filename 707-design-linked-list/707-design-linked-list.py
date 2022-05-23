class MyLinkedList:

    def __init__(self):
        self.val = 0
        self.next = None
        self.tail = self
        self.head = self
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        if index == self.length - 1:
            return self.tail.val
        
        temp = self.head
        while temp != None and index > 0:
            temp = temp.next
            index -= 1
        
        return temp.val

    def addAtHead(self, val: int) -> None:
        if self.length == 0:
            self.val = val
            self.length += 1
            return
        temp = MyLinkedList()
        temp.val = val
        temp.next = self.head
        self.head = temp
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.val = val
            self.length += 1
            return
        temp = MyLinkedList()
        temp.val = val
        temp.tail = None
        self.tail.next = temp
        self.tail = temp
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return 
        
        temp = self.head
        while index > 1:
            temp = temp.next
            index -= 1
        temp2 = MyLinkedList()
        temp2.val = val
        temp2.next = temp.next
        temp.next = temp2
        self.length += 1
        
    def deleteAtIndex(self, index: int) -> None:
        last = False
        if index == 0:
            self.head = self.head.next           
            self.length -= 1
            return
        elif index == 0 and self.length == 1:
            self.length = 0
            return
        elif index >= self.length:
            return
        elif index == self.length-1:
            last = True
            
        temp = self.head
        while temp != None and index > 1:
            temp = temp.next
            index -= 1
        if last:
            temp.next = None
            self.tail = temp
        else:
            temp.next = temp.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)