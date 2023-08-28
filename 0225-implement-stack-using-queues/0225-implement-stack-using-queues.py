class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)        
    
    def pop(self) -> int:
        if self.q1:
            full, empty = self.q1, self.q2
        else:
            full, empty = self.q2, self.q1
        
        while len(full) > 1:
            empty.append(full.popleft())
        
        return full.popleft()

    def top(self) -> int:
        if self.q1:
            full, empty = self.q1, self.q2
        else:
            full, empty = self.q2, self.q1
        
        while len(full) > 1:
            empty.append(full.popleft())
            
        res = full.popleft()
        empty.append(res)
        return res

    def empty(self) -> bool:
        return not (self.q1 or self.q2)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()