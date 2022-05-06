class MyQueue:
    
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while not self.empty():
            self.stack2.append(self.stack.pop())
        
        x = self.stack2.pop()
        while self.stack2 != []:
            self.stack.append(self.stack2.pop())

        return x

    def peek(self) -> int:
        while not self.empty():
            self.stack2.append(self.stack.pop())
        x = self.top()
        while self.stack2 != []:
            self.stack.append(self.stack2.pop())
        return x

    def empty(self) -> bool:
        return self.stack == []

    def top (self) -> int:
        return self.stack2[len(self.stack2)-1]
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()